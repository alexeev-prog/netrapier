from requests import get
from socket import socket, AF_INET, SOCK_DGRAM
import scapy.all as scapy
from ipaddress import IPv4Address
from socket import gethostbyname, gaierror


def ip_from_domain(domain: str) -> (str, None):
    try:
        IPv4Address(domain)
        return domain
    except Exception:
        if domain.startswith("http"):
            domain = domain.split("/")[2]
            if len(domain.split(".")) > 2:
                domain = ".".join(domain.split(".")[1:])

    try:
        ip_domain = gethostbyname(domain)
        return ip_domain
    except gaierror:
        return


def get_devices_in_network():
    target_ip = "192.168.1.1/24"
    # IP Address for the destination
    # create ARP packet
    arp = scapy.ARP(pdst=target_ip)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether / arp

    result = scapy.srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients


def local_ipv4() -> str:
    ip = None
    st = socket(AF_INET, SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        ip = st.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        st.close()
        return ip


def public_ip() -> str:
    try:
        return get('https://api.ipify.org/').text
    except Exception:
        return '127.0.0.1'


