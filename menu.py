"""Provide user with a list of options."""

import pyinputplus as pyip

options_map = {
    1: ["dig", "dig.py",],
    2: ["get kernel and release", "kernel_release.py",],
    3: ["list files", "ls.py",],
    4: ["list groups a user is in", "groups.py",],
    5: ["list free space on mounted disks", "free_space.py",],
    6: ["list users logged in", "users.py",],
    7: ["network name", "get_network_name.py",],
    8: ["ping", "ping.py",],
    9: ["system details", "system_details.py",],
    10: ["traceroute", "traceroute.py",],
    11: ["whois", "whois.py",],
    12: ["exit", "",],
}

NUM_OPTIONS = len(options_map)

while True:
    print("\nplease select an option below.")
    for num, options in options_map.items():
        print(num, options[0])
    response = pyip.inputInt("> ", min=1, max=len(options_map), blank=True)
    if response != len(options_map):
        exec(open(options_map[response][1]).read())
    else:
        print("\nsession complete\n")
        break
