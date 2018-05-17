from scapy.all import *
from threading import Thread, Event
from time import sleep

class Sniffer(Thread):
    def  __init__(self, interface="ens33"):
        super().__init__()

        self.daemon = True

        self.socket = None
        self.interface = interface
        self.stop_sniffer = Event()

    def run(self):
        self.socket = conf.L2listen(
            type=ETH_P_ALL,
            iface=self.interface,
            filter="ip"
        )

        sniff(
            opened_socket=self.socket,
            prn=self.print_packet,
            stop_filter=self.should_stop_sniffer
        )

    def join(self, timeout=None):
        self.stop_sniffer.set()
        super().join(timeout)

    def should_stop_sniffer(self, packet):
        return self.stop_sniffer.isSet()

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

sniffer = Sniffer()

print("[*] Start sniffing...")
sniffer.start()

try:
    while True:
        sleep(100)
except KeyboardInterrupt:
    print("[*] Stop sniffing")
    sniffer.join(2.0)

    if sniffer.isAlive():
        sniffer.socket.close()
