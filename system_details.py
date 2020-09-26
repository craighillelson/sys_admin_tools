from functions import (os,
                       platform,
                       print_return)

print("\nsystem details")
specs = platform.uname()
print(f"system: {specs.system}")
print(f"release: {specs.release}")
print(f"network name: {specs.node}")
processor = platform.processor()
print(f"processor: {processor}")
os.system(f"echo 'public ip address:' "
          f"$(dig +short myip.opendns.com @resolver1.opendns.com)")
os.system(f"echo 'private ip address: '$(ifconfig | grep 'inet ' | "
          f"grep -v 127.0.0.1 | cut -d\  -f2)")
