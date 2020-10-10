"""Prompt user for a hostname and run dig for that hostname."""

import os
from functions import get_hostname

hostname = get_hostname()
response = os.system(f"dig {hostname}")
