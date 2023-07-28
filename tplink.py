#!/usr/bin/env python3

import subprocess
import argparse

parser = argparse.ArgumentParser(description="A script to manage driver installation and system updates.")
parser.add_argument("--install", action="store_true", help="Install the driver.")
parser.add_argument("--sysupdate", action="store_true", help="Update the package lists.")
parser.add_argument("--sysupgrade", action="store_true", help="Upgrade all installed packages.")
parser.add_argument("--ifstatus", action="store_true", help="check the status of the drivers.")
args = parser.parse_args()

if args.install:
    subprocess.run(["sudo", "apt", "install", "realtek-rtl88xxau-dkms", "-y"], check=True)

if args.sysupdate:
    subprocess.run(["sudo", "apt", "update"], check=True)

if args.sysupgrade:
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

if args.ifstatus:
    subprocess.run(["sudo","airmon-ng"], check=True)
