__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import os
import sys
import IO_thread


sys.path.insert(0, 'c:/python34/MyProjects/gui-by-ini/guibyini')
sys.path.insert(0, 'c:/python34/MyProjects/pic-rename/pic-rename')
import SpawnGuiFromIni




#######################################################################################################################
# Determine project path and auto-set debug log file and gui configuration file names as appropriate
#######################################################################################################################
projectPath = os.path.split(__file__)
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'gui_setup.ini'))




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
# Define Data types
#######################################################################################################################
class ApplicationIO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]




#######################################################################################################################
# Define Data tags used for interlocking between application window and IO monitor threads
#######################################################################################################################
IoTable = ApplicationIO()
IoTableCache = ApplicationIO()
IoTableOS = ApplicationIO()

AppWindowObject = SpawnGuiFromIni.AppWindow(guiIniFile, debugLogFile, IoTable)



#######################################################################################################################
# Start IO monitor thread
#######################################################################################################################
enable_thread_2 = True

if enable_thread_2 == True:
    IoThread = IO_thread.IoMonitor(IoTable, IoTableCache, IoTableOS, debugLogFile, AppWindowObject)
    logging.info('[Main] Spawning IO monitor thread (thread-2)')

    IoThread.daemon = True
    logging.info('[Main] IoThread daemon flag set to "True"')

    IoThread.start()
    logging.info('[Main] IoThread started')
else:
    pass




#######################################################################################################################
# Start application window thread
#######################################################################################################################
enable_thread_3 = True

if enable_thread_3 == True:
    SpawnGuiFromIni.AppWindow.SpawnAppWindow(AppWindowObject)
