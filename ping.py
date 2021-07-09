"""Prompt user for a hostname to ping and a number of pings to send."""

import os
import sys
import pyinputplus as pyip
from functions import get_hostname
from tee import StdoutTee


def get_results():
    print("\n")
    return os.system(f"\nping -c {num_pings} {hostname}")


def output_results():
    with StdoutTee("ping.txt", "a", 1):
        if response == 0:
            sys.stdout.write(f"\n{hostname} is up")
        else:
            sys.stdout.write(f"\n{hostname} is down")
        print("\n")


hostname = get_hostname()
num_pings = pyip.inputInt("enter a number pings\n> ")
response = get_results()
output_results()
