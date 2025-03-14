import socket

from typing import Dict


PORTS_SERVICES = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"
}


def is_open_port(target: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        s.close()
    except (socket.gaierror, TimeoutError):
        return port, {
            'status': "Закрыт",
            'comment': PORTS_SERVICES.get(port, 'Неизвестный порт')
        }
    else:
        return port, {
            'status': "Открыт",
            'comment': PORTS_SERVICES.get(port, 'Неизвестный порт')
        }



