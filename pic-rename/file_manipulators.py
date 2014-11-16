__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import os





#######################################################################################################################
# Define class
#######################################################################################################################
class FileManip(object):
    def __init__(self, basedir, logfile):
        self.basedir = basedir
        self.dirToScan = str()
        self.logfile = logfile
        self.filelist = []
        
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', 
                            filename=self.logfile, filemode='w')
        logging.info('[FileRename(object init) logger started')
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
        logging.info('[RenameFiles] Counters reset')
        logging.info('[FileRename(object init) complete')




#######################################################################################################################
# Define method for finding files to modify, including sub-directories under the root
#######################################################################################################################
    def findFilesRootOnly(self):
        self.basedir = self.basedir.replace('\\', '/')
        self.basedir = self.basedir.replace('\n', '')
        logging.info('[RenameFiles(method)] Called with path %s' % self.basedir)
        for file in os.listdir(self.basedir):
            self.file_wp = os.path.join(self.basedir, file)
            if os.path.isfile(self.file_wp):
                logging.info('[findFilesRootOnly(method)] Found: %s' % self.file_wp)
                self.filelist.append(self.file_wp)
            else:
                pass
        return self.filelist




#######################################################################################################################
# Define method for finding files to modify, including sub-directories under the root
#######################################################################################################################
    def findFilesIncludingSubs(self):
        self.basedir = self.basedir.replace('\\', '/')
        self.basedir = self.basedir.replace('\n', '')
        logging.info('[RenameFiles(method)] Called with path %s' % self.basedir)
        for root, dirs, files in os.walk(os.path.normcase(self.basedir)):
            for file in files:
                self.file_wp = os.path.join(root, file)
                if os.path.isfile(self.file_wp):
                    logging.info('[findFilesIncludingSubs(method)] Found: %s' % self.file_wp)
                    self.filelist.append(self.file_wp)
                else:
                    pass
        return self.filelist




#######################################################################################################################
# Check file type against list of acceptable file-types to modify
#######################################################################################################################
    def checkFileExt(self, file, whitelist):
        self.file = os.path.normcase(file)
        self.whitelist = whitelist

        logging.info('[checkFileExt(method)] Checking file: %s' % self.file)
        self.fileRoot, self.fileExt = os.path.splitext(file)
        self.fileExt = self.fileExt.replace('.', '')

        if self.fileExt in self.whitelist:
            logging.info('[checkFileExt(method)] File-type valid for conversion')
            return True
        else:
            logging.info('[checkFileExt(method)] Invalid file-type for conversion')
            return False




#######################################################################################################################
# Extract file attributes
#######################################################################################################################
    def genNewFileName(self, file):
        import os
        import time

        self.file = file
        self.filePath, self.fileName = os.path.split(file)
        logging.info('[genNewFileName(method)] Starting with: %s' % self.fileName)

        info = os.stat(self.file)
        utc_mod_time = time.gmtime(info.st_mtime)

        self.nfileName = ('(' + str(time.strftime('%Y', utc_mod_time)) + '-'
                          + str(time.strftime('%m', utc_mod_time)) + '-'
                          + str(time.strftime('%d', utc_mod_time)) + ')_'
                          + str(time.strftime('%H', utc_mod_time)) + 'h'
                          + str(time.strftime('%M', utc_mod_time)) + 'm'
                          + str(time.strftime('%S', utc_mod_time)) + 's_'
                          + str(info.st_size) + 'b')

        self.newfile = os.path.join(self.filePath, self.nfileName)
        logging.info('[genNewFileName(method)] Converted to: %s' % self.nfileName)

        return self.newfile


