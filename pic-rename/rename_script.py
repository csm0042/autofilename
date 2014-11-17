__author__ = 'Christopher'

import file_manipulator
import logging
import os

class rename_script(object):
    def __init__(self, path, logfile):
        self.path = path
        self.logfile = logfile
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[rename_script.__init__] Logger started')

        self.file = str()
        self.newfile = str()
        self.mainipulator_object = file_manipulator.file_manipulator(str(path), logfile)
        self.extOk = False
        self.include_sub_folders = True
        self.validExt = ['jpg', 'jpeg', 'bmp', 'png', 'gif']

        self.run()



    def run(self):
        if self.include_sub_folders == True:
            logging.info('[rename_script.run] Including sub-folders')
            self.filelist = self.mainipulator_object.return_files_including_subs()
        else:
            logging.info('[rename_script.run] NOT Including sub-folders')
            self.filelist = self.mainipulator_object.return_files_root_only()

        for self.file in self.filelist:
            logging.info('[rename_script.run] Checking: %s' % self.file)
            self.extOk = self.mainipulator_object.return_valid_file_ext(os.path.normcase(self.file), self.validExt)

            if self.extOk == True:
                logging.info('[rename_script.run] Filetype is valid for conversion')
                self.newfile = self.mainipulator_object.generate_filename(self.file)
                logging.info('[rename_script.run] Ideal file name: %s' % self.newfile)
            else:
                logging.info('[rename_script.run] Filetype is NOT valid for conversion')

            if self.extOk == True and self.newfile != self.file:
                logging.info('[rename_script.run] File needs to be re-named')
            else:
                logging.info('[rename_script.run] File name is already correct')

            if os.path.isfile(self.newfile) == True:
                logging.info('[rename_script.run] Collision detected with existing file')