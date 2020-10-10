"""List files in the current directory."""

import os
from functions import print_return

print_return()
response = os.system("ls -la")
print_return()
