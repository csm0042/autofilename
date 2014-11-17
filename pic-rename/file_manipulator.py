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
class file_manipulator(object):
    def __init__(self, basedir, logfile):
        self.basedir = basedir
        self.dirToScan = str()
        self.logfile = logfile
        self.filelist = []
        
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', 
                            filename=self.logfile, filemode='w')
        logging.info('[file_manipulator.__init__] Logger started')
        self.path = str()

        self.filePath = str()
        self.fileName = str()
        self.nfileName = str()
        self.newfile = str()

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
        logging.info('[file_manipulator.__init__] Counters reset')
        logging.info('[file_manipulator.__init__] complete')




#######################################################################################################################
# Define method for finding files to modify, including sub-directories under the root
#######################################################################################################################
    def return_files_root_only(self):
        self.basedir = self.basedir.replace('\\', '/')
        self.basedir = self.basedir.replace('\n', '')
        for file in os.listdir(self.basedir):
            self.file_wp = os.path.join(self.basedir, file)
            if os.path.isfile(self.file_wp):
                self.filelist.append(self.file_wp)
            else:
                pass
        return self.filelist




#######################################################################################################################
# Define method for finding files to modify, including sub-directories under the root
#######################################################################################################################
    def return_files_including_subs(self):
        self.basedir = self.basedir.replace('\\', '/')
        self.basedir = self.basedir.replace('\n', '')
        for root, dirs, files in os.walk(os.path.normcase(self.basedir)):
            for file in files:
                self.file_wp = os.path.join(root, file)
                if os.path.isfile(self.file_wp):
                    self.filelist.append(self.file_wp)
                else:
                    pass
        return self.filelist




#######################################################################################################################
# Check file type against list of acceptable file-types to modify
#######################################################################################################################
    def return_valid_file_ext(self, file, whitelist):
        self.file = os.path.normcase(file)
        self.whitelist = whitelist

        self.fileRoot, self.fileExt = os.path.splitext(file)
        self.fileExt = self.fileExt.replace('.', '')

        if self.fileExt in self.whitelist:
            return True
        else:
            return False




#######################################################################################################################
# Extract file attributes
#######################################################################################################################
    def generate_filename(self, file):
        self.file = os.path.normcase(file)

        self.fileRoot, self.fileExt = os.path.splitext(self.file)
        self.filePath, self.fileName = os.path.split(self.fileRoot)

        info = os.stat(self.file)
        utc_mod_time = time.gmtime(info.st_mtime)

        self.nfileName = ('(' + str(time.strftime('%Y', utc_mod_time)) + '-'
                          + str(time.strftime('%m', utc_mod_time)) + '-'
                          + str(time.strftime('%d', utc_mod_time)) + ')_'
                          + str(time.strftime('%H', utc_mod_time)) + 'h'
                          + str(time.strftime('%M', utc_mod_time)) + 'm'
                          + str(time.strftime('%S', utc_mod_time)) + 's_'
                          + str(info.st_size) + 'b' + self.fileExt)

        self.newfile = os.path.join(self.filePath, self.nfileName)

        return self.newfile


