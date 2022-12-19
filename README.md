A program to impress your friends as if you were a "hacker" from a hollywood movie.

### What exactly it does
Installs needed packages, then it opens terminal (or konsole if your on kde)
Runs tmux, splits window in 4 panes and in each one run a random text based program from the list.
The sample programs are just system monitors or ip monitors or just 'tree /' command, so it looks cool.

### Packages/Sample programs
These packages need to be installed on your system before running fake-hacker.py: python3, python3-dev, python3-pip
These packages will be installed automatically when your run fake-hacker.py (need root perm):
tmux
htop
cmatrix
ifstat
nload
top
nmon
glances


When i fisnished this, I realised that someone's already written this type of program lol.

### Note
If your OS doesnt use apt, dnf or zypper, install all needed packages by yourself and in the script remove lines: 126 and 13-27

### Screenshot

![f1](https://user-images.githubusercontent.com/78962948/208488486-7b10f396-cdbe-4f05-8f51-3ed28f29d2cb.png)
