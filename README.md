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

### Download/Usage
```
1? - To Download this from github:
    git clone https://github.com/1RaY-1/fake-hacker

2? Install needed python modules to run this:
    cd fake-hacker/
    pip3 install -r requierements.txt
    
  And run this program:
    python3 fake-hacker.py
```

### Note
If this program throws an error saying "Your package manager isn't supported", install all needed packages by yourself and in the script remove lines: 126 and 13 to 27

### Screenshot

![f1](https://user-images.githubusercontent.com/78962948/208488486-7b10f396-cdbe-4f05-8f51-3ed28f29d2cb.png)



When i fisnished this, I found that someone's already written this type of program lol.
