"""List files in the current directory."""

from functions import (os,
                       platform,
                       print_return)

kernel = platform.system()
release = platform.release()
print(f"\nkernel: {kernel}")
print(f"release: {release}\n")
