"""Prompt user for a hostname to ping and a number of pings to send."""

from functions import (get_hostname,
                       os,
                       print_return)

hostname = get_hostname()
response = os.system(f"dig {hostname}")
