"""Prompt user for a hostname to ping and a number of pings to send."""

from functions import (get_hostname,
                       os,
                       pyip,
                       print_return)

hostname = get_hostname()
num_pings = pyip.inputInt("enter a number pings\n> ")
print_return()

response = os.system(f"ping -c {num_pings} {hostname}")
if response == 0:
    print(f"\n{hostname} is up\n")
else:
    print(f"\n{hostname} is down\n")
