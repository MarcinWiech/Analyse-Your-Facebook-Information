#!/usr/bin/env python3
# import the library
from appJar import gui
from main import main
# create a GUI variable called app

dirs = ['a', 'a']

def press(button):
    
    if button == "Exit":
        app.stop()
    elif button == "Select Facebook Folder":
        dirs[0] = app.directoryBox(title=None, dirName=None, parent=None)
    elif button == "Save Result to":
        dirs[1] = app.directoryBox(title=None, dirName=None, parent=None)
    elif button == "Run":
        if dirs[0] != 'a' and dirs[1] != 'a':
            app.setLabel("status", "Running")
            main(dirs[0], dirs[1])
            app.setLabel("status", "Finished")
        else:
            app.setLabel("status", "Select directories")
            print("NO")


app = gui()
app.setBg("White")
app.addLabel("title", "Welcome to Facebook Analyzer")
app.setLabelBg("title", "White")
app.addButtons(["Select Facebook Folder", "Save Result to"], press)
app.addButtons(["Run", "Exit"], press)
app.addEmptyLabel("status")
app.go()