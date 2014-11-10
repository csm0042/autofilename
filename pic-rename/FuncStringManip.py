# FUNCTION: ReplaceSlash
# This funtion will take a directory path in the form of a string and search
# it for backslashes.  When found, it will replace them with forward slashes
# since that is what python expects
#
def ReplaceSlash (InputPath):
        OutputPath = InputPath.replace('\\', '/');
        return OutputPath
