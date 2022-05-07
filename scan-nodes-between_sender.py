from scapy.all import *;
reciever= input("IP of reciever: ");
requested= input("IP requested: ");
maxNodeNum= int(input("how many nodes to consider?"));
eachNum= int(input("how many packets to send for each node?"))
SHARED_ID=0xaf;
SHARED_RAW= "abcdefghijklmnopqrstuvwxyzABC123";
for i in range(maxNodeNum):
    n= i+1;
    for j in range(eachNum): send(IP(src=reciever, dst=requested, ttl=n)/ICMP(type=8, seq=n, id=SHARED_ID)/SHARED_RAW, verbose=False);
    print(f"sent {eachNum} package(s) for node number {n}");
print(f"finished sending {maxNodeNum} packages");