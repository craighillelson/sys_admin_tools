"""List files in the current directory."""

from functions import (os,
                       print_return)

print_return()
response = os.system(f"ls -la")
print_return()
