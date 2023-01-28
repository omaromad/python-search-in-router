
import scapy.all as scapy
import pyfiglet
import re
import sys
import time
text = pyfiglet.figlet_format("OMAR SRCH")
print (text)
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_add_range_entered = ("192.168.98.1")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} serch ip address  range")
        break

arp_result = scapy.arping(ip_add_range_entered)
