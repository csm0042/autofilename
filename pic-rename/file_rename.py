__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import os
import time




#######################################################################################################################
# Define class
#######################################################################################################################
class FileRename(object):
    def __init__(self, basedir, logfile):
        self.basedir = basedir
        self.logfile = logfile
        
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', 
                            filename=self.logfile, filemode='w')
        logging.info('[FileRename(object init) logger started')
        self.path = str()

        self.filename_wp_we = str()
        self.filename_wp_ne = str()
        self.filename_np_we = str()
        self.filename_np_ne = str()
        self.filename_ext = str()

        self.nfilename_wp_we = str()
        self.nfilename_wp_ne = str()
        self.nfilename_np_we = str()
        self.nfilename_np_ne = str()
        self.nfilename_ext = str()
        self.nfilename_wp_we_mem = str()


        self.count = 0
        self.already = 0
        self.modifiedCount = 0
        self.dirCount = 0
        self.skipCount = 0
        self.index = 0
        logging.info('[RenameFiles] Counters reset')
        logging.info('[FileRename(object init) complete')


#######################################################################################################################
# Define method for modifying file names
#######################################################################################################################
    def RunLoop(self):
        logging.info('[RenameFiles(method)] Called with path %s' % self.basedir)
        for root, dirs, files in os.walk(self.basedir):
            logging.info('[RenameFiles(method)] Root: %s' % root)
            logging.info('[RenameFiles(method)] dir: %s' % dirs)
            logging.info('[RenameFiles(method)] files: %s' % files)



