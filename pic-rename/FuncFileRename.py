# FUNCTION: RenameByDateAndSize
# This function is fed a filename and returns the file created and modified timestamps
# along with the size of the file.  All inputs are assumed to be type "string"
#
def RenameByDateAndSize(FileExt, year, month, day, hour, minute, second, size):
        import os
        Filename = "(" + year + "-" + month + "-" + day + ")_" + hour + 'h' + minute + 'm' + second + "s_" + size + "b" + "." + FileExt
        return Filename
