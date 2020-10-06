"""
Send a request to a Web site to check check connectivity and gather network 
details.
"""

import requests
import socket
import netifaces as ni


def check_connectivity():
    response = requests.get("https://espn.com")
    return response.status_code == 200


if check_connectivity() == True:
    print("good to go")
else:
    print("something is off")

print("\nNetworking Details")

hostname = socket.gethostname()
print(f"Hostname: {hostname}")

external_ip = requests.get("https://api.ipify.org").text
print(f"External IP: {external_ip}")

ni.ifaddresses('en0')
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
print(f"Internal IP: {ip}")

import netifaces as ni
addrs = ni.ifaddresses('en0')
addrs[ni.AF_INET]
mac = addrs[ni.AF_LINK]
for mac_addrs in mac[0].values():
    print(f"MAC address: {mac_addrs}")

gws = ni.gateways()[ni.AF_INET][0]
print(f"Gateway: {gws[0]}\n")
