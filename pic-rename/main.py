__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import configparser
import logging
import os
import sys
import thread1_gui


sys.path.insert(0, 'c:/python34/MyProjects/gui-by-ini/guibyini')
sys.path.insert(0, 'c:/python34/MyProjects/pic-rename/pic-rename')





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
startime = time.time()
logging.info('[Main] Program Logger Started at t = 0.0000')
logging.info('[Main] Logging to file: %s' % debugLogFile)
logging.info('[Main] Using GUI configuration file: %s' % guiIniFile)




#######################################################################################################################
# Define Data types
#######################################################################################################################
class ApplicationIO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]














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
logging.info('[Main] Spawning Application window thread (thread-1)')
Thread1 = thread1_gui.Appwindow(guiIniFile, debugLogFile, appWindowIoTable)
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