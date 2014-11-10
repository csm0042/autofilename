# FUNCTION: GetFileAtt
# This function is fed a filename and returns the key file attributes associated with that file
#
def GetFileAtt(filename):
        import os
        mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(filename)
        return mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime
#
#
# FUNCTION: Split filename into filename and extension (type)
# This function is fed a filename and returns the file created and modified timestamps
# along with the size of the file.  All inputs are assumed to be type "string"
#
def ExtractFileExt(FileNameStr):
        Location = FileNameStr.rfind(".")
        if Location != -1:
                Pointer1 = Location+1
                Pointer2 = Location
                FileExtension = FileNameStr[Pointer1:]
                FileNameWOExtension = FileNameStr[0:Pointer2]
        else:
                FileExtension = "error"
        return FileNameWOExtension, FileExtension
