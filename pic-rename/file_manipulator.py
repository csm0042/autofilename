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
        self.whitelist = []
        
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', 
                            filename=self.logfile, filemode='w')
        logging.info('[file_manipulator.__init__] Logger started')
        self.path = str()

        self.file_path = str()

        self.filename_wp_we = str()
        self.filename_wp_ne = str()
        self.filename_np_we = str()
        self.filename_np_ne = str()
        self.filename_ext = str()

        self.new_filename_wp_we = str()
        self.new_filename_wp_ne = str()
        self.new_filename_np_we = str()
        self.new_filename_np_ne = str()
        self.new_filename_ext = str()

        self.new_filename_wp_we_mem = str()

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
            self.filename_wp_we = os.path.join(self.basedir, file)
            if os.path.isfile(self.filename_wp_we):
                self.filelist.append(self.filename_wp_we)
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
                self.filename_wp_we = os.path.join(root, file)
                if os.path.isfile(self.filename_wp_we):
                    self.filelist.append(self.filename_wp_we)
                else:
                    pass
        return self.filelist




#######################################################################################################################
# Check file type against list of acceptable file-types to modify
#######################################################################################################################
    def return_valid_file_ext(self, file, whitelist):
        self.filename_wp_we = os.path.normcase(file)
        self.whitelist = whitelist

        self.filename_wp_ne, self.filename_ext = os.path.splitext(self.filename_wp_we)
        self.filename_ext = self.filename_ext.replace('.', '')

        if self.filename_ext in self.whitelist:
            return True
        else:
            return False




#######################################################################################################################
# Extract file attributes
#######################################################################################################################
    def generate_filename(self, file):
        self.filename_wp_we = os.path.normcase(file)

        self.filename_wp_ne, self.filename_ext = os.path.splitext(self.filename_wp_we)
        self.file_path, self.filename_np_ne = os.path.split(self.filename_wp_ne)
        self.filename_ext = self.filename_ext.replace('.', '')

        info = os.stat(self.filename_wp_we)
        utc_mod_time = time.gmtime(info.st_mtime)

        self.new_filename_np_ne = ('(' + str(time.strftime('%Y', utc_mod_time)) + '-'
                          + str(time.strftime('%m', utc_mod_time)) + '-'
                          + str(time.strftime('%d', utc_mod_time)) + ')_'
                          + str(time.strftime('%H', utc_mod_time)) + 'h'
                          + str(time.strftime('%M', utc_mod_time)) + 'm'
                          + str(time.strftime('%S', utc_mod_time)) + 's_'
                          + str(info.st_size) + 'b')
        
        self.new_filename_np_we = self.new_filename_np_ne + '.' + self.filename_ext
        self.new_filename_wp_we = os.path.join(self.file_path, self.new_filename_np_we)
        
        return self.new_filename_wp_we




#######################################################################################################################
# Increment filename
#######################################################################################################################
    def increment_filename(self, file, index):
        self.new_filename_wp_we = os.path.normcase(file)
        self.index = index

        self.new_filename_wp_ne, self.new_filename_ext = os.path.splitext(self.new_filename_wp_we)
        self.new_filename_ext = self.new_filename_ext.replace('.', '')
        self.new_filename_wp_we = self.new_filename_wp_ne + '(' + str(self.index) + ').' + self.new_filename_ext
        self.new_filename_wp_we = os.path.normcase(self.new_filename_wp_we)

        return self.new_filename_wp_we


