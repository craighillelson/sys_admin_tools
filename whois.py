"""Prompt user for a hostname to ping and a number of pings to send."""

from functions import (get_name,
                       os,
                       pyip,
                       print_return)

hostname = get_name(f"\nenter hostname\n> ")
print_return()
response = os.system(f"whois {hostname}")
