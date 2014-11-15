__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import linecache
import sys
sys.path.insert(0, 'c:/python34/MyProjects/gui-by-ini/guibyini')
import SpawnGuiFromIni
import threading
import time



#######################################################################################################################
# Define IO Monitoring class and thread
#######################################################################################################################
class IoMonitor(threading.Thread):
    def __init__(self, realIO, IOcache, IOos, logfile, appWindowObject):
        self.lastLineRead = 1
        self.lineFromLog = str()
        self.realIO = realIO
        self.IOcache = IOcache
        self.IOos = IOos
        self.logfile = logfile
        self.appWindowObject = appWindowObject
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[thread2_IO.init] Program Logger for thread-2 started')
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.lineFromLog = linecache.getline(self.logfile, self.lastLineRead)
            if self.lineFromLog != "":
                SpawnGuiFromIni.AppWindow.write_text(self.appWindowObject, 1, self.lineFromLog)
                self.lastLineRead += 1
            else:
                linecache.clearcache()
                pass
            time.sleep(0.20)


