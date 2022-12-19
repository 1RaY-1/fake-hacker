#!/usr/bin/env python3

import os
import random
from time import sleep

# from requirements.txt
try:
    import pyautogui
except ImportError:
    exit("Missing module: pyautogui\nType: 'pip3 install pyautogui' to install it")

# get the package manager
# debian/ubuntu/etc... (apt)
if int (os.system("command -v apt") ) == 0:
    pm = "apt" # [P]ackage [M]anager
# fedora/centos (dnf)
elif int (os.system("command -v dnf") ) == 0:
    pm = "dnf"
# older fedora (yum)
elif int (os.system("command -v yum") ) == 0:
    pm = "yum"
# opensuse (zypper)
elif int (os.system("command -v zypper") ) == 0: 
    pm = "zypper"
else:
    exit("Your package manager isn't supported!")

class FakeHacker:

    def __init__(self):
        self.packages = ["tmux", "htop", "cmatrix", "ifstat", "nload", "top", "nmon", "glances"]
        self.program1 = None
        self.program2 = None
        self.program3 = None
        self.program4 = None
        self.extra1 = []
        self.extra2 = []
        self.extra3 = []
        self.extra4 = []

    def intro(self):
        print("When you eventually have 4 programs opened in tmux, to exit all these just press ALT + F4")
        input("(Press ENTER to continue)\n")

    def install_packages(self):
        for e in self.packages:
            if int (os.system("command -v " + e) ) != 0:
                print("Installing package: " + e)
                sleep(1.5)
                os.system(f"sudo {pm} install {e} -y")

#   function to open terminal
    def open_cmd(self):
        pyautogui.press('winleft')
        sleep(0.7) # just in case, use a small delay
        # now, in kde the terminal is called 'konsole' and in other environments 'terminal'
        desktop = os.environ.get('DESKTOP_SESSION')
        if 'kde' in desktop:
            pyautogui.write('konsole')
        else:
            pyautogui.write('terminal')
        sleep(0.7)
        pyautogui.press('enter')
        sleep(0.7)

    def choose_all(self):
        self.packages.remove("tmux")
        self.packages.remove("ifstat")
        self.packages.append("ifstat -l -t") # <-- to show time and other thing
        self.packages.append("tree /") # <-- just list all files of the computer, because it looks cool
        self.packages = random.sample(self.packages, k=len(self.packages)) # should mix the order a little
        
        self.program1 = self.packages.pop()
        if self.program1 == "nmon": # <-- in nmon we need to choose an option by pressing a specific key
            self.extra1.append("c") # <-- so this is a key to press (only once)
        self.program2 = self.packages.pop()
        if self.program2 == "nmon":
            self.extra2.append("c")
        self.program3 = self.packages.pop()
        if self.program3 == "nmon":
            self.extra3.append("c")
        self.program4 = self.packages.pop()
        if self.program4 == "nmon":
            self.extra4.append("c")

    def do_it(self):
        pyautogui.write('tmux')
        pyautogui.press('enter')
        pyautogui.press('f11')

        # now open cool stuff:
        #1
        pyautogui.write(self.program1)
        pyautogui.press('enter')
        if self.extra1 != []:
            pyautogui.press(self.extra1)
            sleep(0.6)
        #2
        pyautogui.hotkey('ctrl', 'b', '%') # <-- create a new pane
        pyautogui.write(self.program2)
        pyautogui.press('enter')
        if self.extra2 != []:
            pyautogui.press(self.extra2)
            sleep(0.6)
        #3 
        pyautogui.hotkey('ctrl', 'b', '"') # <-- another pane
        pyautogui.write(self.program3)
        pyautogui.press('enter')
        if self.extra3 != []:
            pyautogui.press(self.extra3)
            sleep(0.6)
        #4
        # comeback to first pane first
        pyautogui.hotkey('ctrl', 'b')
        pyautogui.press('left')
        pyautogui.hotkey('ctrl', 'b', '"')
        pyautogui.write(self.program4)
        pyautogui.press('enter')
        if self.extra4 != []:
            pyautogui.press(self.extra4)
            sleep(0.6)

    def main(self):
        fh.intro()
        fh.install_packages()
        fh.open_cmd()
        fh.choose_all()
        fh.do_it()

if __name__ == '__main__':
    fh = FakeHacker()
    fh.main()
