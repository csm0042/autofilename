__author__ = 'chris.maue'

import logging
import os
import sys
sys.path.append("c:/Python34/MyProjects/guibyini/guibyini")
import SpawnGuiFromIni
import threading


# Determine project path and auto-set debug log file and gui configuration file names as appropriate
projectPath = os.path.split(__file__)
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'gui.ini'))


# Start program logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debugLogFile,
                    filemode='w')
logging.info('Program Logger Started')


# Define Class to create and run application window in a separate thread
class AppWindow(threading.Thread):
    def __init__(self, inifile):
        self.IniFile = inifile
        threading.Thread.__init__(self)

    def run(self):
        import tkinter as tk
        self.root=tk.Tk()
        SpawnGuiFromIni.SpawnAppWindow(self.root, self.IniFile)
        self.root.title('My Application Window')
        self.root.mainloop()


# Spawn Gui Thread
logging.info('Spawning app window in separate thread')
appWindowThread = AppWindow(guiIniFile)
logging.info('Starting app window thread')
appWindowThread.start()
logging.info('App window thread started and running')