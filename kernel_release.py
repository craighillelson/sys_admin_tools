"""Output the kernel and release."""

import platform

kernel = platform.system()
release = platform.release()
print(f"\nkernel: {kernel}")
print(f"release: {release}\n")
