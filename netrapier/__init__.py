from typing import List
from concurrent.futures import ThreadPoolExecutor

from netrapier.design import Ui_MainWindow
from netrapier.constants import VERSION, LINK
from netrapier.modules.portscan import is_open_port

from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QRunnable, Slot, QThreadPool


class PortScannerWorker(QRunnable):
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

    def _start_port_scan(self, ip_addr: str, port_range_for_scan: List[int]):
        self.scanning = True

        self.ui.start_port_scan_btn.setEnabled(False)

        total_ports_count = port_range_for_scan[1] - port_range_for_scan[0]
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(total_ports_count)

        ports = [port for port in range(port_range_for_scan[0] + 1, port_range_for_scan[1] + 1)]

        ports_names = {}

        with ThreadPoolExecutor(max_workers=len(ports)) as executor:  # Устанавливаем максимальное количество потоков
            futures = {executor.submit(is_open_port, ip_addr, port): port for port in ports}
            for future in futures:
                port, status = future.result()
                self.ui.progressBar.setValue(port)
                ports_names[port] = status

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

        worker = PortScannerWorker(self._start_port_scan, ip_addr=self.ui.port_scanner_ip_line.text(),
                                   port_range_for_scan=port_range_for_scan)

        self.threadpool.start(worker)
