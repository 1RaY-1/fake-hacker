A program to impress your friends as if you were a "hacker" from a hollywood movie.

### What exactly it does
Installs needed packages, then it opens terminal (or konsole if your on kde)
Runs tmux, splits window in 4 panes and in each one runs a random text based program from the list.

The sample programs are just system monitors or ip monitors or just 'tree /' command, so it looks cool.

### Supported OS
This only supports **Linux**, with a Desktop Environment.

***If you are using something like I3WM or QTILE that doesn't have DE integrated, then this script needs to be changed to work properly***

### Packages/Sample programs
Make sure you have this installed before running fake-hacker.py: ```python3```, ```python3-dev```, ```python3-pip```

These packages will be installed automatically when your run fake-hacker.py (need root perm):
```tmux```,
```htop```,
```cmatrix```,
```ifstat```,
```nload```,
```top```,
```nmon```,
```glances```

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


### Screenshot

![f1](https://user-images.githubusercontent.com/78962948/208488486-7b10f396-cdbe-4f05-8f51-3ed28f29d2cb.png)
