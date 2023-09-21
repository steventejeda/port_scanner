import socket


def scan(target, ports):
    for port in range(1, ports):
        scan_port(targets, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened" + str(port))
        sock.close()
    except:
        pass 

targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_address in targets.split(','):
        scan(ip_address.strip(' '), ports)
else:
    scan(targets, ports)