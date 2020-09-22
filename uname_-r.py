"""List files in the current directory."""

from functions import (os,
                       print_return)

print_return()
os.system("echo kernel")
kernel = os.system("uname")
print_return()
os.system("echo release")
release = os.system("uname -r")
print_return()
