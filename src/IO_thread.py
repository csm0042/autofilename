__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import linecache
import threading
import time



#######################################################################################################################
# Define IO Monitoring class and thread
#######################################################################################################################
class monitor_io(threading.Thread):
    def __init__(self, realIO, IOcache, IOos, logfile, gui_object):
        self.last_line_read = 1
        self.lineFromLog = str()
        self.realIO = realIO
        self.IOcache = IOcache
        self.IOos = IOos
        self.logfile = logfile
        self.gui_object = gui_object
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[thread2_IO.init] Program Logger for thread-2 started')
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.lineFromLog = linecache.getline(self.logfile, self.last_line_read)
            while len(self.lineFromLog) != 0:
                self.gui_object.write_text(2, self.lineFromLog)
                self.last_line_read += 1
                self.lineFromLog = linecache.getline(self.logfile, self.last_line_read)
            linecache.clearcache()
            time.sleep(0.20)


