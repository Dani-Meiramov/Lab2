import re

ip_addresses = dict()
log = open('access.log', 'r')

for elem in log:
    k = re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', elem)
    if k:
        ip_address = k.group()
        n = ip_address.rindex('.')
        subnetwork = ip_address[:n]
        if subnetwork in ip_addresses:
            ip_addresses[subnetwork].add(ip_address)
        else:
            ip_addresses[subnetwork] = {ip_address}

for subnetwork in ip_addresses.keys():
    for ip in ip_addresses[subnetwork]:
        print(ip)
    print()