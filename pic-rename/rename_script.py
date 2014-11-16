__author__ = 'Christopher'

import file_manipulators

class rename_script(object):
    def __init__(self, path, logfile):
        self.path = path
        self.logfile = logfile
        self.fileManipObject = file_manipulators.FileManip(str(path), logfile)
        self.includeSubFolders = True
        self.validExt = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
        self.run()

    def run(self):

        if self.includeSubFolders == True:
            self.filelist = self.fileManipObject.findFilesIncludingSubs()
        else:
            self.filelist = self.fileManipObject.findFilesRootOnly()

        for file in self.filelist:
            self.extOk = self.fileManipObject.checkFileExt(file, self.validExt)

            if self.extOk == True:
                self.newFile = self.fileManipObject.genNewFileName(file)

            if self.extOk == True and self.newFile != file:
                # file is of the wrong format and needs to be modified

                pass
            else:
                pass