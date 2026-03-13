import nmap

scanner = nmap.PortScanner()

print("Scanning... please wait.")
scanner.scan('127.0.0.1', '22-80')

for host in scanner.all_hosts():
    print(f"Host found: {host}")
    print(f"State: {scanner[host].state()}")