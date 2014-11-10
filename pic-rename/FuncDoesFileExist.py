# FUNCTION: GetFileAtt
# This function is fed a filename and returns the key file attributes associated with that file
#
import os

def open_if_not_exists(filename):
    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except:
        print "Ooops"
        return None
    fobj = os.fdopen(fd, "w")
    return fobj
