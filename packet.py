from scapy.all import *

def pkt_callback(pkt):
        pkt.show() # debug statement

        sniff(iface="ens33", prn=pkt_callback, filter="tcp", store=0)
