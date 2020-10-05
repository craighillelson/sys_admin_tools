"""Send a request to a Web site to check check connectivity."""

import requests


def check_connectivity():
    response = requests.get("https://espn.com")
    return response.status_code == 200


if check_connectivity() == True:
    print("good to go")
else:
    print("something is off")
