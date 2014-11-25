__author__ = 'Christopher'

from .file_manipulator import *
import logging
import os

class rename_script(object):
    def __init__(self, path, logfile, types, include):
        self.path = path
        self.logfile = logfile
        self.types = types.lower()
        self.include = include.lower()

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[rename_script.__init__] Logger started')

        self.manipulator_object = file_manipulator(str(path), logfile)
        self.filename_wp_we = str()
        self.new_filename_wp_we_mem = str()

        self.result_int = int()
        self.include_int = self.include.find('yes', 0, len(self.include))
        if self.include_int != (-1):
            self.include_sub_folders = True
        else:
            self.include_sub_folders = False

        self.extOk = False
        self.types = self.types.replace(' ', '')
        self.types = self.types.replace(';', ',')
        self.types = self.types.replace(':', ',')
        self.types = self.types.replace('\n', '')
        self.types = self.types.rstrip(',')
        self.validExt = self.types.split(',')

        self.total_count = int()
        self.dir_count = int()
        self.type_count = int()
        self.modified_count = int()
        self.already_count = int()

        self.run()



    def run(self):
        if self.include_sub_folders == True:
            logging.info('[rename_script.run] Including sub-folders')
            self.filelist = self.manipulator_object.return_files_including_subs()
        else:
            logging.info('[rename_script.run] NOT Including sub-folders')
            self.filelist = self.manipulator_object.return_files_root_only()
            
        
        for self.filename_wp_we in self.filelist:
            self.total_count += 1

            # Check to determine if this is a file (not a directory)
            if os.path.isfile(self.filename_wp_we):
                self.step_pointer = 1
            else:
                self.step_pointer = 991


            # Check file extension to see if file-type is in the whitelist
            if self.step_pointer == 1:
                logging.info('[rename_script.run] Checking file-type of: %s' % self.filename_wp_we)
                self.extOk = self.manipulator_object.return_valid_file_ext(os.path.normcase(self.filename_wp_we),
                                                                           self.validExt)
                if self.extOk == True:
                    logging.info('[rename_script.run] File-type is valid')
                    self.step_pointer = 2
                else:
                    logging.info('[rename_script.run] File-type is NOT valid')
                    self.step_pointer = 992


            # Generate revised filename based upon current rule-set
            if self.step_pointer == 2:
                self.new_filename_wp_we = self.manipulator_object.generate_filename(self.filename_wp_we)
                if os.path.normcase(self.filename_wp_we) == os.path.normcase(self.new_filename_wp_we):
                    self.step_pointer = 4
                else:
                    logging.info('[rename_script.run] File-name is NOT valid')
                    self.step_pointer = 3


            # Check to see if desired file-name is already in-use
            if self.step_pointer == 3:
                if os.path.isfile(self.new_filename_wp_we) == True:
                    logging.info('[rename_script.run] Name collision detected with existing file')
                    self.step_pointer = 5
                else:
                    logging.info('[rename_script.run] Desired file-name is available')
                    self.step_pointer = 6

            # Check to see if file-names match because they are the same file
            if self.step_pointer == 4:
                if os.path.samefile(self.new_filename_wp_we, self.filename_wp_we):
                    logging.info('[rename_script.run] File-name is valid')
                    self.step_pointer = 993
                else:
                    logging.info('[rename_script.run] Name collision detected with existing file')
                    self.step_pointer = 5


            # Add index number to tail-end of filename to make unique
            if self.step_pointer == 5:
                self.index = 0
                self.new_filename_wp_we_mem = self.new_filename_wp_we
                while os.path.isfile(self.new_filename_wp_we) == True:
                    self.index += 1
                    self.new_filename_wp_we = self.manipulator_object.increment_filename(self.new_filename_wp_we_mem,
                                                                                         self.index)
                logging.info('[rename_script.run] Next available file-name: %s' % self.new_filename_wp_we)
                self.step_pointer = 6


            # Perform file rename operaton
            if self.step_pointer == 6:
                os.rename(self.filename_wp_we, self.new_filename_wp_we)
                logging.info('[rename_script.run] File rename operation successful')
                self.step_pointer = 7


            # Increment counters for logger
            if self.step_pointer == 7:
                self.modified_count += 1
                self.step_pointer = 9999

            if self.step_pointer == 991:
                self.dir_count += 1
                self.step_pointer = 9999

            if self.step_pointer == 992:
                self.type_count += 1
                self.step_pointer = 9999


            if self.step_pointer == 993:
                self.already_count += 1
                self.step_pointer = 9999

        logging.info('[rename_script.run] RESULTS')
        logging.info('[rename_script.run] %d Total objects' % self.total_count)
        logging.info('[rename_script.run] %d Total objects modified' % self.modified_count)
        logging.info('[rename_script.run] %d Total objects skipped because they are not files' % self.dir_count)
        logging.info('[rename_script.run] %d Total objects skipped due to invalid type' % self.type_count)
        logging.info('[rename_script.run] %d Total objects skipped because they are already properly formatted'
                     % self.already_count)

        
