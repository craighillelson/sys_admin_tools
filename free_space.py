"""Get free space on mounted disks."""

import shutil

disk_space = shutil.disk_usage("/")
free_space = disk_space.free / disk_space.total * 100
print(f"\npercentage of free space on disk: {round(free_space, 2)}%\n")
