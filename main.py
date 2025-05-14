import socket
import subprocess
import platform
import os
import requests
import psutil


def ping_test(host="8.8.8.8", count=4):
    print(f"\n[+] Pinging {host}...")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), host]
    subprocess.run(command)


def dns_resolution(domain):
    print(f"\n[+] Resolving domain: {domain}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] {domain} resolved to {ip}")
    except socket.gaierror:
        print("[-] DNS resolution failed.")


def traceroute(host):
    print(f"\n[+] Tracerouting {host}...")
    command = "tracert" if platform.system().lower() == "windows" else "traceroute"
    subprocess.run([command, host])


def port_scan(host, ports=[22, 80, 443]):
    print(f"\n[+] Scanning ports on {host}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        status = "Open" if result == 0 else "Closed"
        print(f"Port {port}: {status}")
        sock.close()


def check_internet():
    print("\n[+] Checking internet connectivity...")
    try:
        requests.get("https://www.google.com", timeout=5)
        print("[+] Internet is reachable.")
    except requests.ConnectionError:
        print("[-] Internet is not reachable.")


def network_info():
    print("\n[+] Network interface information:")
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        print(f"\nInterface: {interface_name}")
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")


def main():
    while True:
        print("\nNetwork Troubleshooting Toolkit")
        print("1. Ping Test")
        print("2. DNS Resolution")
        print("3. Traceroute")
        print("4. Port Scan")
        print("5. Internet Connectivity Check")
        print("6. Network Interface Info")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            host = input("Enter host to ping: ")
            ping_test(host)
        elif choice == "2":
            domain = input("Enter domain to resolve: ")
            dns_resolution(domain)
        elif choice == "3":
            host = input("Enter host for traceroute: ")
            traceroute(host)
        elif choice == "4":
            host = input("Enter host for port scan: ")
            ports = input("Enter comma-separated ports (default: 22,80,443): ")
            ports = [int(p.strip()) for p in ports.split(",")] if ports else [22, 80, 443]
            port_scan(host, ports)
        elif choice == "5":
            check_internet()
        elif choice == "6":
            network_info()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
