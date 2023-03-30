import subprocess
import sys
import os


def req() -> None:
    modules = ["PySide6", "sympy"]

    os_name = os.name

    if os_name == "nt":
        for module in modules:
            try:
                __import__(module)
            except:
                subprocess.run(f"pip install {module}", shell=True)
    else:
        for module in modules:
            try:
                __import__(module)
            except:
                subprocess.run(f"pip3 install {module}", shell=True)

if __name__ == "__main__":
    req()