"""Prompt user for a hostname and run dig for that hostname."""

from functions import (get_hostname,
                       os)

hostname = get_hostname()
response = os.system(f"dig {hostname}")
