from typing import List
from concurrent.futures import ThreadPoolExecutor

from netrapier.design import Ui_MainWindow
from netrapier.constants import VERSION, LINK
from netrapier.modules.portscan import is_open_port
from netrapier.modules.pkganalyzing import analyze_packet, create_report, is_suspicious, is_alarming
from netrapier.modules.networkinfo import get_devices_in_network, local_ipv4, public_ip, ip_from_domain

import scapy.all as scapy
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QRunnable, Slot, QThreadPool


def split_list(original_list, max_size=10):
    return [original_list[i:i + max_size] for i in range(0, len(original_list), max_size)]


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        self.fn(*self.args, **self.kwargs)


class NetRapierWindow(QMainWindow):
    def __init__(self):
        super(NetRapierWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()

        self.scanning = False

        self.setWindowTitle(f'NetRapier {VERSION} - {LINK}')
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.ui.start_port_scan_btn.clicked.connect(self.start_port_scan)
        self.ui.start_pkg_analyzing_btn.clicked.connect(self.start_package_analyzing)
        self.ui.get_net_info_btn.clicked.connect(self.get_net_info)
        self.ui.get_domain_name_btn.clicked.connect(self.get_domain_name)

    def get_domain_name(self):
        domain = self.ui.enter_domain_line.text()
        self.ui.ip_addr_by_domain_lbl.setText(f'Domain: {domain}. IP: {ip_from_domain(domain)}')

    def _get_net_info(self):
        self.ui.public_ip_addr_lbl.setText(f'Ваш публичный IP-адрес: {public_ip()}')
        self.ui.local_ip_addr_lbl.setText(f'Ваш публичный IP-адрес: {local_ipv4()}')
        self.ui.ip_addr_default_lbl.setText('Ваш IP адрес шлюза по умолчанию: Заблокировано настройками приватности')

        line = 0
        for client in get_devices_in_network():
            self.ui.get_net_info_btn.setItem(line, 0, QTableWidgetItem(client['ip']))
            self.ui.get_net_info_btn.setItem(line, 1, QTableWidgetItem(client['mac']))
            line += 1

    def get_net_info(self):
        worker = Worker(self._get_net_info)

        self.threadpool.start(worker)

    def _start_package_analyzing(self):
        captured_packets = []
        self.ui.start_pkg_analyzing_btn.setEnabled(False)
        self.ui.port_scan_table.setRowCount(0)

        def packet_callback(packet):
            packet_info = analyze_packet(packet)
            captured_packets.append(packet_info)

        try:
            scapy.sniff(prn=packet_callback, store=0, timeout=60)
        except Exception as e:
            return False

        good_line = 0
        bad_line = 0
        line = -1

        self.ui.pkg_analyze_result.setText(f'Пакетов проанализировано: {len(captured_packets)}')

        self.ui.good_pkgs_table.setRowCount(len(captured_packets))
        for entry in captured_packets:
            if is_suspicious(entry) or is_alarming(entry):
                table = self.ui.bad_pkgs_table
                bad_line += 1
                line = bad_line
            else:
                table = self.ui.good_pkgs_table
                good_line += 1
                line = good_line

            table.setItem(line, 0, QTableWidgetItem(entry['time'].strftime('%H:%M:%S')))
            table.setItem(line, 1, QTableWidgetItem(entry['src_ip']))
            table.setItem(line, 2, QTableWidgetItem(entry['dst_ip']))
            table.setItem(line, 3, QTableWidgetItem(entry['protocol']))
            table.setItem(line, 4, QTableWidgetItem(entry['length']))

        report_name = create_report(captured_packets)

        self.ui.label_6.setText(f'Анализ активности пакетов: репорт сохранен в {report_name}')
        self.ui.start_pkg_analyzing_btn.setEnabled(True)

    def start_package_analyzing(self):
        worker = Worker(self._start_package_analyzing)

        self.threadpool.start(worker)

    def _start_port_scan(self, ip_addr: str, port_range_for_scan: List[int]):
        self.scanning = True
        self.ui.port_scan_table.setRowCount(0)
        self.ui.progressBar.setValue(0)
        self.ui.start_port_scan_btn.setEnabled(False)

        total_ports_count = port_range_for_scan[1] - port_range_for_scan[0]
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(total_ports_count)

        ports = [port for port in range(port_range_for_scan[0] + 1, port_range_for_scan[1] + 1)]

        list_with_ports = split_list(ports, 2500)

        ports_names = {}

        for sublist in list_with_ports:
            with ThreadPoolExecutor(max_workers=len(sublist)) as executor:
                try:
                    futures = {executor.submit(is_open_port, ip_addr, port): port for port in sublist}
                    for future in futures:
                        port, status = future.result()
                        self.ui.progressBar.setValue(port)
                        ports_names[port] = status
                except Exception:
                    continue

        line = 0

        self.ui.port_scan_table.setRowCount(len(ports_names))

        for port, data in ports_names.items():
            self.ui.port_scan_table.setItem(line, 0, QTableWidgetItem(str(port)))
            self.ui.port_scan_table.setItem(line, 1, QTableWidgetItem(data['status']))
            self.ui.port_scan_table.setItem(line, 2, QTableWidgetItem(data['comment']))
            line += 1

        self.ui.start_port_scan_btn.setEnabled(True)
        self.scanning = False

    def start_port_scan(self):
        if self.scanning:
            button = QMessageBox.warning(
                self,
                "Предупреждение",
                "Сканирование портов уже идет, подождите пожалуйста.",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
            return

        if len(self.ui.port_scanner_ip_line.text()) < 7:
            button = QMessageBox.critical(
                self,
                "Ошибка Ввода IP-адреса",
                "Вы не ввели IP адрес корректной длины.",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
            return

        port_range_for_scan = self.ui.port_scanner_diap_line.text().strip().replace(' ', '').split('-')

        if len(port_range_for_scan) < 2:
            button = QMessageBox.critical(
                self,
                "Ошибка Ввода диапазона портов",
                "Вы ввели некорректный диапазон портов. Укажите в следующем формате: x-y, где x начало, а y конец. "
                "Например: 1-8000.",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
            return
        elif not port_range_for_scan[0].isdigit() or not port_range_for_scan[1].isdigit():
            button = QMessageBox.critical(
                self,
                "Ошибка Ввода диапазона портов",
                "Вы ввели не целочисленные значения.",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
            return

        port_range_for_scan[0] = int(port_range_for_scan[0])
        port_range_for_scan[1] = int(port_range_for_scan[1])

        if port_range_for_scan[1] <= port_range_for_scan[0]:
            button = QMessageBox.critical(
                self,
                "Ошибка Ввода диапазона портов",
                "Конечное число диапазона должно быть больше первого",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
            return

        if port_range_for_scan[0] < 0 or port_range_for_scan[1] > 65536:
            button = QMessageBox.critical(
                self,
                "Ошибка Ввода диапазона портов",
                "Диапазон не должен начинаться с отрицательного значения или быть выше 65536",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
            return

        if port_range_for_scan[1] >= 20000:
            button = QMessageBox.critical(
                self,
                "Предупреждение",
                "Большие диапазоны могут привлечь к плохой работе приложения.",
                buttons=QMessageBox.Ok | QMessageBox.Cancel,
                defaultButton=QMessageBox.Ok,
            )

            if button == QMessageBox.Cancel:
                return

        worker = Worker(self._start_port_scan, ip_addr=self.ui.port_scanner_ip_line.text(),
                                   port_range_for_scan=port_range_for_scan)

        self.threadpool.start(worker)
