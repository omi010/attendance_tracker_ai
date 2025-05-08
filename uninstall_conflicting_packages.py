"""
Utility script to remove any conflicting packages from the virtual environment.
Run this once to clean up any conflicting packages.
"""
import subprocess
import sys

def uninstall_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package_name])
    print(f"Successfully uninstalled {package_name}")

if __name__ == "__main__":
    # List of potentially conflicting packages
    conflicting_packages = ["app"]
    
    for package in conflicting_packages:
        try:
            uninstall_package(package)
        except Exception as e:
            print(f"Failed to uninstall {package}: {e}")
    
    print("\nIf there were any conflicting packages, they have been removed.")
    print("You should now be able to run the application without import conflicts.")
