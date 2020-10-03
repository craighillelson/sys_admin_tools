"""Prompt user for a hostname and send a whois command for that hostname."""

from functions import (get_name,
                       os,
                       pyip,
                       print_return)

hostname = get_name(f"\nenter hostname\n> ")
print_return()
response = os.system(f"whois {hostname}")
