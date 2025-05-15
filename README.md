# network-troubleshooting-tool

🧰 Network Troubleshooting Toolkit – Documentation

📌 Overview

The Network Troubleshooting Toolkit is a command-line utility written in Python that provides essential tools for diagnosing network issues. It can perform actions like ping tests, DNS resolution, traceroute, port scanning, internet connectivity checks, and retrieving local network interface information.
________________________________________
📦 Requirements

Before running the toolkit, install the following Python packages:

bash

pip install requests psutil urllib3
________________________________________
🛠️ Features

1. Ping Test
   
 Send ICMP echo requests to a specified host to check connectivity.

•	Function: ping_test(host, count)

•	Usage: Sends 4 ping requests (default) to the given host.
________________________________________
2. DNS Resolution
   
 Resolve a domain name to its corresponding IP address.
 
•	Function: dns_resolution(domain)

•	Usage: Useful to test DNS response and verify resolution.
________________________________________
3. Traceroute

 Track the path that a packet takes to reach the destination host.
 
•	Function: traceroute(host)

•	Usage: Identifies intermediate hops to a target address.
________________________________________
4. Port Scanner
   
 Scans a host for open or closed TCP ports.

•	Function: port_scan(host, ports)

•	Default Ports Scanned: 22 (SSH), 80 (HTTP), 443 (HTTPS)
________________________________________
5. Internet Connectivity Check
   
 Verifies if the system can access the internet.
 
•	Function: check_internet()

•	Usage: Pings Google (https://www.google.com) to determine connectivity.
________________________________________
6. Network Interface Info
   
 Displays IP, subnet, and broadcast details of all local network interfaces.
 
•	Function: network_info()

•	Library Used: psutil
________________________________________
🧑‍💻 How to Use

Run the script using:

bash

python main.py

You'll see a menu with options:

markdown

Network Troubleshooting Toolkit
1. Ping Test
2. DNS Resolution
3. Traceroute
4. Port Scan
5. Internet Connectivity Check
6. Network Interface Info
0. Exit
Enter a number to choose the desired tool and follow the prompts.
________________________________________
💡 Example

Port Scan Example Input:

java

Enter host for port scan: scanme.nmap.org

Enter comma-separated ports (default: 22,80,443): 22,80

Output:

Port 22: Open
Port 80: Closed
________________________________________
🔐 Permissions Note

•	Traceroute and Ping may require elevated permissions on some systems.

•	For Linux/macOS, you may need to use sudo.
________________________________________
🧰 Dependencies

Library	Purpose

socket	Low-level networking (DNS, ports)

subprocess	Run system-level commands (ping, traceroute)

requests	HTTP request for connectivity check

psutil	Retrieve network interface info

urllib3	Dependency for requests

