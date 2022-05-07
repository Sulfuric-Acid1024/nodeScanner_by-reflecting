SHARED_ID=0xaf;
SHARED_RAW= "abcdefghijklmnopqrstuvwxyzABC123";

from scapy.all import *;

recieved_array= [];
for i in range(100): recieved_array.append([]);
def sniffed(pkt):
    if (not ICMPerror in pkt) or (not IPerror in pkt):
        return ;
    if pkt[ICMP].type != 11 : # message of TTL exception
        return ;
    if pkt[ICMPerror].id == SHARED_ID:
        recieved_array[pkt[ICMPerror].seq].append(pkt);
        print(f"recieved packet {pkt[ICMPerror].seq}");
    return ;
try:
    sniff(filter="icmp", prn=sniffed);
except KeyboardInterrupt:
    (1==1); # do nothing
for i in range(100):
    print(f"node {i}: recieved {len(recieved_array[i])}");
    for pkt in recieved_array[i]:
        print(f"\tpacket from {pkt[IP].src}: {'common reply' if pkt[ICMP].type == 0 else ('TTL exceeded' if pkt[ICMP].type == 11 else 'unknown type '+str(pkt[ICMP].type))}");
    time.sleep(0.5); # make it possible for the user to stop the program half-way printing