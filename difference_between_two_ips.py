#This program received two IPv4 addresses, and returns the number of addresses between them including the first
#one and excluding last one.

def ip_to_int(ip):
    parts = map(int, ip.split('.'))
   
    return sum(part << (8*(3-i)) for i, part in enumerate(parts))

def count_ips(first, last):
    return ip_to_int(last) - ip_to_int(first)
   
print(count_ips("10.0.0.0", "10.0.0.50"))
print(count_ips("10.0.0.0", "10.0.1.0"))