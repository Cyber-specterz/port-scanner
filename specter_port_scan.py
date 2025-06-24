#!/usr/bin/env python3
import socket
import sys

# ASCII banner
def banner():
    print(r"""
   _____                  _             _____           _     
  / ____|                | |           / ____|         | |    
 | (___   ___  _   _ _ __| |_ _   _   | (___  _   _ ___| |__  
  \___ \ / _ \| | | | '__| __| | | |   \___ \| | | / __| '_ \ 
  ____) | (_) | |_| | |  | |_| |_| |   ____) | |_| \__ \ | | |
 |_____/ \___/ \__,_|_|   \__|\__, |  |_____/ \__, |___/_| |_|
                               __/ |           __/ |          
                              |___/           |___/           
    🕵️ Tool: SpecterPortScan  | 📷 IG: @cyber_specterz
    """)

# Port scanner
def scan(target, ports):
    print(f"\n[+] Scanning target: {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan aborted by user.")
            sys.exit()
        except socket.error:
            print("[!] Couldn't connect to server.")
            sys.exit()

# Entry point
if __name__ == "__main__":
    banner()
    if len(sys.argv) != 2:
        print("Usage: python3 specter_port_scan.py <target-ip>")
        sys.exit()
    
    target_ip = sys.argv[1]
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    scan(target_ip, common_ports)
