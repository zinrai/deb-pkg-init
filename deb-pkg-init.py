#!/usr/bin/env python3

import os
import subprocess
import sys
import shutil

def main():
    deb_email = input("Enter DEBEMAIL: ")
    deb_fullname = input("Enter DEBFULLNAME: ")

    os.environ['DEBEMAIL'] = deb_email
    os.environ['DEBFULLNAME'] = deb_fullname

    current_dir = os.path.basename(os.getcwd())

    package_version = input("Enter package version (e.g., 1.0): ")

    if not shutil.which("dh_make"):
        print("Error: dh_make command not found.")
        sys.exit(1)

    try:
        subprocess.run(["dh_make", "-p", f"{current_dir}_{package_version}", "--createorig"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"dh_make command failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
