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
    def RenameFiles(self):
        logging.info('[RenameFiles(method)] Called with path %s' % self.basedir)
        for root, dirs, files in os.walk(self.basedir):
            logging.info('[RenameFiles(method)] Root: %s' % root)
            logging.info('[RenameFiles(method)] dir: %s' % dirs)
            logging.info('[RenameFiles(method)] files: %s' % files)
            for filename in files:

                self.count += 1
                self.filename_np_we = filename
                self.filename_wp_we = os.path.normcase(os.path.join(root, self.filename_np_we))
                logging.info('[RenameFiles(method)] Found file: %s' % self.filename_wp_we)

                # Determine if this is a file or directory
                if os.path.isfile(self.filename_wp_we):
                    logging.info('[RenameFiles(method)] Item is a file (not a directory)')

                    # Determine file type
                    self.filename_wp_ne, self.filename_ext = os.path.splitext(self.filename_wp_we)
                    self.path, self.filename_np_ne = os.path.split(self.filename_wp_ne)
                    logging.info('[RenameFiles(method)] File name is: %s' % self.filename_np_ne)
                    logging.info('[RenameFiles(method)] File extension is: %s' % self.filename_ext)
                    
                    if (self.filename_ext == "jpg" or self.filename_ext == "JPG" or self.filename_ext == "bmp"
                        or self.filename_ext == "BMP" or self.filename_ext == "png" or self.filename_ext == "PNG"
                        or self.filename_ext == "gif" or self.filename_ext == "GIF"):
                        logging.info('[RenameFiles(method)] File type valid for conversion')

                        # Look up additional file attributes
                        self.fileAttrib = os.stat(self.filename_wp_we)

                        self.nfilename_np_ne = ("(" + str(time.strftime("%Y", self.fileAttrib.st_mtime)) + "-"
                                                + str(time.strftime("%m", self.fileAttrib.st_mtime)) + "-"
                                                + str(time.strftime("%d", self.fileAttrib.st_mtime)) + ")_"
                                                + str(time.strftime("%H", self.fileAttrib.st_mtime)) + 'h'
                                                + str(time.strftime("%M", self.fileAttrib.st_mtime)) + 'm'
                                                + str(time.strftime("%S", self.fileAttrib.st_mtime)) + "s_"
                                                + str(self.fileAttrib.st_size) + "b")

                        self.nfilename_np_we = self.nfilename_np_ne + self.filename_ext
                        self.nfilename_wp_we = os.path.join(self.path, self.nfilename_np_we)
                        logging.info("[RenameFiles(method)] New file name with path: %s" % self.nfilename_wp_we)

                        # Determine if the file needs to be renamed
                        if (self.nfilename_wp_we != self.filename_wp_we):
                            logging.info('[RenameFiles(method)] Filename is not of the proper format')

                            self.index = 0
                            self.nfilename_wp_we_mem = self.nfilename_wp_we

                            while os.path.isfile(self.nfilename_wp_we):
                                if not os.path.samefile(self.filename_wp_we, self.nfilename_wp_we):
                                    logging.info('[RenameFiles(method)] Filename %s is already in use' % self.nfilename_wp_we_mem)
                                    self.index += 1
                                    self.nfilename_wp_we = self.nfilename_wp_ne + '(' + str(self.index) + ')' + self.nfilename_ext
                                else:
                                    pass
                                    #break

                            # Perform actual file rename operation once a valid filename is found that isn't already in use
                            os.rename(self.filename_wp_we, self.nfilename_wp_we)
                            logging.info("[RenameFiles(method)] Renaming file to: %s" % self.nfilename_wp_we)
                            self.modifiedCount += + 1
                        else:
                            # Increment counter for files that already met proper naming convention
                            self.already += 1
                            logging.info('[RenameFiles(method)] Filename is already in the proper format')
                    else:
                        # Increment counter for items skipped because they are not the correct file type
                        self.skipCount += 1
                        logging.info('[RenameFiles(method)] Not a valid file type for conversion')
                else:
                    # Increment counter for items skipped because they are directories (not files)
                    self.dirCount += 1
                    logging.info('[RenameFiles(method)] Skipping because item is a directory')


        logging.info("[RenameFiles(method)] %d total objects" % self.count)
        logging.info("[RenameFiles(method)] %d files were updated" % self.modifiedCount)
        logging.info("[RenameFiles(method)] %d skipped because they are directories" % self.dirCount)
        logging.info("[RenameFiles(method)] %d skipped because they are already properly named" % self.already)
        logging.info("[RenameFiles(method)] %d skipped because they are not a picture" % self.skipCount)


