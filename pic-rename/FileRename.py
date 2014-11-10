# PROGRAM: Main_File_Rename_V3.00.00.py
# Last Modified: 2014-10-08
# Last Modified by: C. Maue
#
# CHANGELOG
# v1.00.00	2014-10-05	Initial program
# v2.00.00	2014-10-07	Program re-structured to use function calls instead of hard-coding everything in a single file
# v3.00.00	2014-10-08	Added logging support
#
# PROGRAM SUMMARY
# This program will scan through a directory looking for pictures.  When found, it will check the file name of the picture to
# determine if it is of the form "(yyyy-mm-dd)_xxh_yym_zzs_aaaaaab" where:
# yyyy = four-digit year from file-modified attribute
# mm = two-digit month from file-modified attribute
# dd = two-digit date from file-modified attribute
# xx = two-digit hour
# yy = two-digit minute
# zz = two-digit second
# aaaaaa = size of file (in bytes)
#
# If the filename is not of the correct format, the program will automatically rename it to the proper format based upon its attributes.
# If the filename already exists, it will automatically add a "(x)" to the end of the filename where x = a sequential number starting at 1.  This
# number will be incremented as necessary to make the filename unique so files are not overwritten.
#
# When run, the user is prompted for the directory to scan.  Once entered, the program will automatically scan that directory AND all sub-directories
# (top-down) for files to rename.  Only certain file types are supported, all other files are ignored.
#
# ENABLE LOGGING
# The following will set up logging for debugging purposes
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename='C:/Users/cmaue/OneDrive/Programming/_File_Rename.log',
                    filemode='w')
#
# **************************************************************************************
# BEGIN MAIN PROGRAM
# **************************************************************************************
#
# Import libraries
import os
import sys
import datetime
#
# Time-stamp logfile with time program was run
StartTime = datetime.datetime.now()
logging.info('Program Started at: %s' % str(StartTime))
#
# Import user-created functions
import FuncStringManip
import FuncConvertTime
import FuncFileAttrib
import FuncFileRename
#
# Prompt user for root directory to scan
print (" ")
print (" ")
basedir = input('Please enter the directory path to scan: ')
logging.info("Path: %s" % basedir)
#
# Reset diagnostic counters
Count = 0
Already = 0
ModifiedCount = 0
DirCount = 0
SkipCount = 0
logging.info("Counters Reset")
#
# Display "working" message so user knows something is happening
print('')
print('Working.......')
print('')
#
# The following lines of code will search the directory structure for all of the files to check/update, then cycle through those files
# checking and updateding each as necessarywill create a list of files with paths working from top to bottom starting at the base directory
for root, dirs, files in os.walk(basedir):
	for filename in files:
		Count = Count + 1
		OriginalFileName = filename
		# Convert "\" to "/" since that's what python uses for its 
		OriginalFileNameWithPath = os.path.join(root, filename)
		logging.info("Found file: %s" % OriginalFileNameWithPath)
		# Determine if this is a file or directory
		if os.path.isfile(OriginalFileNameWithPath):
			logging.info('Item is a file (not a directory)')
			# Determine file type
			FileNameWOExt, FileExt = FuncFileAttrib.ExtractFileExt(OriginalFileNameWithPath)
			if (FileExt == "jpg" or FileExt == "JPG" or FileExt == "bmp" or FileExt == "BMP" or FileExt == "png" or FileExt == "PNG" or FileExt == "gif" or FileExt == "GIF"):
				logging.info('Filetype valid for conversion')
				# Look up additional file attributes
				mode1, ino1, dev1, nlink1, uid1, gid1, size1, atime1, mtime1, ctime1 = FuncFileAttrib.GetFileAtt(OriginalFileNameWithPath)
				# Determine Various Date/Time attribute values for file modified date
				TM, TM_Year, TM_Month, TM_Day, TM_Hour, TM_Minute, TM_Second = FuncConvertTime.DisasembleStructTime(mtime1)
                # Generate new filename
				NewFileName = FuncFileRename.RenameByDateAndSize(FileExt, TM_Year, TM_Month, TM_Day, TM_Hour, TM_Minute, TM_Second, str(size1))
				# Append base path to new filename
				NewFileNameWithPath = os.path.join(root, NewFileName)
				logging.info("Original file name with path: %s" % OriginalFileNameWithPath)
				logging.info("New file name with path: %s" % NewFileNameWithPath)
				# Determine if the file needs to be renamed
				if (NewFileNameWithPath != OriginalFileNameWithPath):
					logging.info('Filename is not of the proper format')
					index = 0
					NewFileNameWithPathChecked = NewFileNameWithPath
					while os.path.isfile(NewFileNameWithPathChecked):
						logging.info('Filename %s is already in use' % NewFileNameWithPathChecked)
						#logging.warn("Filename: %s is already in use" % str(FuncStringManip.ReplaceSlash(NewFileNameWithPath)))
						NewFileNameWOExt, NewFileExt = FuncFileAttrib.ExtractFileExt(NewFileNameWithPath)
						index = index + 1
						NewFileNameWithPathChecked = NewFileNameWOExt + '(' + str(index) + ').' + NewFileExt						
					# Perform actual file rename operation once a valid filename is found that isn't already in use
					os.rename(OriginalFileNameWithPath, NewFileNameWithPathChecked)
					logging.info("Renaming file to: %s" % NewFileNameWithPathChecked)
					ModifiedCount = ModifiedCount + 1
				else:
					# Increment counter for files that already met proper naming convention
					Already = Already + 1
					logging.info('Filename is already in the proper format')
			else:
				# Increment counter for items skipped because they are not the correct filetype
				SkipCount = SkipCount + 1
				logging.info('Not a valid filetype for conversion')
		else:
			# Increment counter for items skipped because they are directories (not files)
			DirCount = DirCount + 1
			logging.info('Skipping because item is a directory')
# Time-stamp logfile with time program was completed
FinishTime = datetime.datetime.now()
ExecutionTime = FinishTime-StartTime
logging.info('Program Finished at: %s' % str(FinishTime))
logging.info('Execution Time: %s' % str(ExecutionTime))
logging.info("%d total objects" % Count)
logging.info("%d files were updated" % ModifiedCount)
logging.info("%d skipped because they are directories" % DirCount)
logging.info("%d skipped because they are already properly named" % Already)
logging.info("%d skipped because they are not a picture" % SkipCount)
print (" ")
print (" ")
print ("Finished")
print ("%d total objects" % Count)
print ("%d files were updated" % ModifiedCount)
print ("%d skipped because they are directories" % DirCount)
print ("%d skipped because they are already properly named" % Already)
print ("%d skipped because they are not a picture" % SkipCount)

