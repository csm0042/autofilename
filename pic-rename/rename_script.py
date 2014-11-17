__author__ = 'Christopher'

import file_manipulator

class rename_script(object):
    def __init__(self, path, logfile):
        self.path = path
        self.logfile = logfile
        self.mainipulator_object = file_manipulator.file_manipulator(str(path), logfile)
        self.includeSubFolders = True
        self.validExt = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
        self.run()

    def run(self):

        if self.includeSubFolders == True:
            self.filelist = self.mainipulator_object.return_files_including_subs()
        else:
            self.filelist = self.mainipulator_object.return_files_root_only()

        for file in self.filelist:
            self.extOk = self.mainipulator_object.return_valid_file_ext(file, self.validExt)

            if self.extOk == True:
                self.newFile = self.mainipulator_object.generate_filenamee(file)

            if self.extOk == True and self.newFile != file:
                # file is of the wrong format and needs to be modified

                pass
            else:
                pass