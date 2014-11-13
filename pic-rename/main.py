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
# Define Application Io data type
#######################################################################################################################
class ApplicationIO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]




#######################################################################################################################
# Define application window class and thread
#######################################################################################################################
class AppWindow(threading.Thread):
    global startime
    def __init__(self, iniFile, logFile, ioTable):
        self.iniFile = iniFile
        self.logFile = logFile
        self.ioTable = ioTable
        threading.Thread.__init__(self)
        logging.info('[Main (thread-1)] Application window init complete at t = +%f' % float(time.time()-startime))

    def run(self):
        self.root=tk.Tk()
        logging.info('[Main (thread-1)] Calling SpawnAppWindow function at t = +%f' % float(time.time()-startime))
        self.app = SpawnGuiFromIni.AppWindow(self.root, self.iniFile, self.logFile, self.ioTable)
        logging.info('[Main (thread-1)] Setting window title at t = +%f' % float(time.time()-startime))
        self.root.title('My Application Window')
        logging.info('[Main (thread-1)] Starting tkinter main loop at t = +%f' % float(time.time()-startime))
        self.root.mainloop()




#######################################################################################################################
# Define IO Monitoring class and thread
#######################################################################################################################
class IOMonitor(threading.Thread):
    global startime
    def __init__(self, realIO, IOcache, IOos, quitCmd, appWindow):
        self.realIO = realIO
        self.IOcache = IOcache
        self.IOos = IOos
        self.quitCommand = quitCmd
        self.appWindow = appWindow
        self.pathText = str()
        threading.Thread.__init__(self)

    def run(self):
        while True:
            for i in range(14):
                if self.realIO.input[i] == self.IOcache.input[i]:
                    self.realIO.input[i] = False
                if self.realIO.input[i] == True and self.IOcache.input[i] == False:
                    logging.info('[Main (thread-2)] F%d pressed at t = +%f' % (int(i), float(time.time()-startime)))
                    self.IOcache.input[i] = True
                    self.IOos.input[i] = True
                elif self.realIO.input[i] == False and self.IOcache.input[i] == True:
                    self.IOcache.input[i] = False

            # Read text field and trigger file rename loop
            if self.IOos.input[2] == True:
                logging.info('[Main (thread-2)] Run button has been pressed at t = +%f' % float(time.time()-startime))
                self.pathText = Thread1.app.tkHandshakeReadText(0)
                print(self.pathText)
                self.IOos.input[2] = False

            # Shut down application and logic loop if "quit" button is pressed in application window
            if self.IOos.input[int(self.quitCommand)] == True:
                self.IOos.input[int(self.quitCommand)] = False
                logging.info('[Main (thread-2)] F%d has been pressed (quit) at t = +%f' %
                             (int(i), float(time.time()-startime)))
                logging.info('[Main (thread-2)] Application is closing')
                self.appWindow.root.destroy()
                sys.exit()

            time.sleep(0.20)




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
# Set up I/O table used by application window (live data, cache, and one-shot)
#######################################################################################################################
appWindowIoTable = ApplicationIO()
appWindowIoTableCache = ApplicationIO()
appWindowIoTableOS = ApplicationIO()




#######################################################################################################################
# Start application window thread
#######################################################################################################################
startime = time.time()

logging.info('[Main] Spawning Application window thread (thread-1)')
Thread1 = AppWindow(guiIniFile, debugLogFile, appWindowIoTable)
Thread1.daemon = False
logging.info('[Main] Thread 1 (application window GUI) daemon flag set to "False"')
Thread1.start()
logging.info('[Main] Thread 1 started')




#######################################################################################################################
# Start IO monitoring thread
#######################################################################################################################
logging.info('[Main] Spawning IO Monitor thread (thread-2)')
Thread2 = IOMonitor(appWindowIoTable, appWindowIoTableCache, appWindowIoTableOS, quitCommand, Thread1)
Thread2.daemon = True
logging.info('[Main] Thread 2 (IO Monitor) daemon flag set to "True"')
Thread2.start()
logging.info('[Main] Thread 2 started')
