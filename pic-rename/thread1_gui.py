__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import sys
sys.path.insert(0, 'c:/python34/MyProjects/gui-by-ini/guibyini')
import SpawnGuiFromIni
import threading



#######################################################################################################################
# Initialize and run thread
#######################################################################################################################
class thread1_gui(threading.Thread):
    def __init__(self, inifile, logfile, iotable):
        self.inifile = inifile
        self.logfile = logfile
        self.iotable = iotable
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[thread1_gui.init] Program Logger for thread-1 started')
        threading.Thread.__init__(self)

    def run(self):
        logging.info('[thread1_gui.run] Calling Appwindow function')
        self.gui = Appwindow(self.inifile, self.logfile, self.iotable)





#######################################################################################################################
# Define application window class and thread
#######################################################################################################################
class Appwindow():
    def __init__(self, inifile, logfile, iotable):
        self.inifile = inifile
        self.logfile = logfile
        self.iotable = iotable
        logging.info('[thread1_gui.Appwindow] Calling SpawnGuiFromIni.SpawnAppwindow function')
        SpawnGuiFromIni.SpawnAppwindow(self.inifile, self.logfile, self.iotable)





