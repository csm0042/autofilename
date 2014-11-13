__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import os
import sys
import tkinter as tk
import threading
import time

sys.path.insert(0, 'c:/python34/MyProjects/gui-by-ini/guibyini')
import configparser
import SpawnGuiFromIni




#######################################################################################################################
# Determine project path and auto-set debug log file and gui configuration file names as appropriate
#######################################################################################################################
projectPath = os.path.split(__file__)
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'gui.ini'))




#######################################################################################################################
# Start program logger / debugger
#######################################################################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debugLogFile,
                    filemode='w')
logging.info('[Main] Program Logger Started')
logging.info('[Main] Logging to file: %s' % debugLogFile)
logging.info('[Main] Using GUI configuration file: %s' % guiIniFile)




#######################################################################################################################
# Get global application parameters from INI file
#######################################################################################################################
Config = configparser.ConfigParser()
Config.read(guiIniFile)
dict1 = {}
options = Config.options('config')
for option in options:
    try:
        dict1[option] = Config.get('config', option)
        if dict1[option] == -1:
            pass
    except:
        dict1[option] = None
quitCommand = dict1['quit command']




#######################################################################################################################
# Define Application Io data type
#######################################################################################################################
class ApplicationIO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]




#######################################################################################################################
# Set up I/O table used by application window (live data, cache, and one-shot)
#######################################################################################################################
appWindowIoTable = ApplicationIO()
appWindowIoTableCache = ApplicationIO()
appWindowIoTableOS = ApplicationIO()




#######################################################################################################################
# Define IO Check Function
#######################################################################################################################
def IOCheck(app, realIO, IOcache, IOos, quitCmd, logfile, lastLineRead):
    while True:
        for i in range(14):
            if realIO.input[i] == IOcache.input[i]:
                realIO.input[i] = False
            if realIO.input[i] == True and IOcache.input[i] == False:
                logging.info('[Main (thread-2)] F%d pressed at t = +%f' % (int(i), float(time.time()-startime)))
                IOcache.input[i] = True
                IOos.input[i] = True
            elif realIO.input[i] == False and IOcache.input[i] == True:
                IOcache.input[i] = False

        # Read text field and trigger file rename loop
        if IOos.input[2] == True:
            logging.info('[Main (thread-2)] Run button has been pressed at t = +%f' % float(time.time()-startime))
            pathText = str(app.readTextField(1))
            app.writeTextField(2, pathText)
            IOos.input[2] = False

        # Shut down application and logic loop if "quit" button is pressed in application window
        if IOos.input[int(quitCmd)] == True:
            IOos.input[int(quitCmd)] = False
            logging.info('[Main (thread-2)] F%d has been pressed (quit) at t = +%f' % (int(i), float(time.time()-startime)))
            logging.info('[Main (thread-2)] Application is closing')
            app.root.destroy()
            sys.exit()


        lineToPrint = str(yieldlines(logfile, lastLineRead))
        if lineToPrint != "":
            app.writeTextField(2, lineToPrint)
            lastLineRead += 1

        root.after(1000, IOCheck)
    return


def picklines(file, lines):
    return [x for i, x in enumerate(file) if i in lines]


def yieldlines(file, lines):
    return (x for i, x in enumerate(file) if i in lines)









#######################################################################################################################
# Start application
#######################################################################################################################
startime = time.time()
line = 0
root=tk.Tk()
logging.info('[Main] Calling SpawnAppWindow function at t = +%f' % float(time.time()-startime))
appWindow = SpawnGuiFromIni.AppWindow(root, guiIniFile, debugLogFile, appWindowIoTable)
logging.info('[Main] Setting window title at t = +%f' % float(time.time()-startime))
root.title('My Application Window')
logging.info('[Main (thread-1)] Starting tkinter main loop at t = +%f' % float(time.time()-startime))
root.after(1000, IOCheck, appWindow, appWindowIoTable, appWindowIoTableCache, appWindowIoTableOS, quitCommand, debugLogFile, line)
root.mainloop()
