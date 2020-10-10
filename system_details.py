import os
import platform
from functions import print_return

print("\nsystem details")
specs = platform.uname()
print(f"system: {specs.system}")
print(f"release: {specs.release}")
print(f"network name: {specs.node}")
processor = platform.processor()
print(f"processor: {processor}")
os.system(f"echo 'uptime:' $(uptime)")
os.system(f"echo 'public ip address:' "
          f"$(dig +short myip.opendns.com @resolver1.opendns.com)")
os.system(f"echo 'private ip address:' $(hostname -I)")
print("\n")
