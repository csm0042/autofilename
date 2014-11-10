# FUNCTION: RenameFileByTimeAndSize
# This function is fed a filename and returns the file created and modified timestamps
# along with the size of the file.  All inputs are assumed to be type "string"
#
def DisasembleStructTime(InputTime):
        import time
        TimeToConvert = time.gmtime(InputTime)
        tm = time.strftime("%Y-%m-%d %H:%M:%S", TimeToConvert)
        tm_year = time.strftime("%Y", TimeToConvert) #tm[0:4]
        tm_month = time.strftime("%m", TimeToConvert)
        tm_day = time.strftime("%d", TimeToConvert)
        tm_hour = time.strftime("%H", TimeToConvert)
        tm_min = time.strftime("%M", TimeToConvert)
        tm_sec = time.strftime("%S", TimeToConvert)
        return tm, tm_year, tm_month, tm_day, tm_hour, tm_min, tm_sec
