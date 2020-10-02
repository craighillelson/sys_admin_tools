"""Get free space on mounted disks."""

from functions import (os,
                       print_return)

print_return()
cmd = "df -h"
output = cmd + str("> free_space.txt")
response = os.system(cmd)
output_file = os.system(output)
print("\n'free_space.txt' exported successfully\n")
