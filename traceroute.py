"""Run traceroute to an address specified by the user."""

from functions import (get_hostname,
                       os,
                       pyip,
                       print_return)

hostname = get_hostname()
print_return()
response = os.system(f"traceroute {hostname}")
