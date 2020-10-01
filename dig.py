"""Prompt user for a hostname and run dig for that hostname."""

from functions import (get_hostname,
                       os,
                       print_return)

hostname = get_hostname()
response = os.system(f"dig {hostname}")
