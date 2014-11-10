# IMPORT REQUIRED LIBRARIES
# The following will import libraries that are required for this program
# ************************************************************************************************************
import logging
import os
import FuncConvertTime
import FuncFileAttrib
import FuncFileRename

# DETERMINE LOCATION OF SCRIPT BEING RUN
# By locating which directory the current script resides in, the program can automatically find the various INI files its needs to configure itself, regardless of paths
# ************************************************************************************************************
path = os.path.split(__file__)
print(path)
path = os.path.dirname(os.path.realpath(__file__))
fileNameWithExt = os.path.basename(__file__)
extPointer = fileNameWithExt.find('.py')
fileName = fileNameWithExt[:extPointer]
# Using the path of the current python script file, set filenames and locations to the main, debug, and gui files
logFileName = fileName + '.log'
logFileNameWithPath = path + '\\' + logFileName
iniFileName = fileName + '.ini'
iniFileNameWithPath = path + '\\' +  iniFileName



# ENABLE LOGGING
# The following will set up logging for debugging purposes
# ************************************************************************************************************
logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(levelname)-8s %(message)s',
					filename=logFileNameWithPath,
					filemode='w')
logging.info('Program Logger Started')


# DEFINE COMMANDS TO MAP TO BUTTONS
# ************************************************************************************************************
def callback_b1():
	path = e1.get()
	logging.info('Rename function called with path: "%s"' % path)
	if os.path.exists(path) and os.path.isdir(path):
		logging.info('Path: "%s" is valid' % path)	
		includeFlag = True
		funcRename(path, includeFlag)
	else:
		logging.info('Path: "%s" does not exist' % path)	
	
def callback_b2():
	try:
		os.system("python C:/Users/cmaue/OneDrive/Programming/Python_Projects/Picture_Rename/FileRename.py")
		logging.info('Call program "FileRename.py"')
	except ImportError:
		logging.info('FileRename.py not found')
		
def funcRename(inputPath, includeSub):
	# Reset diagnostic counters
	Count = 0
	Already = 0
	ModifiedCount = 0
	DirCount = 0
	SkipCount = 0
	logging.info("Counters Reset")
	# Set root folder of directory tree to search
	basedir = inputPath
	# Search for files in directory structure
	if includeSub == True:
		logging.info("searching for files in root folder AND all sub-folders")
		for root, dirs, files in os.walk(basedir):
			Count = Count + 1
	else:
		logging.info("searching for files in root folder ONLY")
		for files in os.listdir(basedir):
			Count = Count + 1
	# process files found
	for filename in files:
		OriginalFileName = filename
		# Convert "\" to "/" since that's what python uses for its 
		OriginalFileNameWithPath = os.path.join(root, filename)
		logging.info("Found file: %s" % OriginalFileNameWithPath)
		# Determine if this is a file or directory
		if os.path.isfile(OriginalFileNameWithPath):
			logging.info('Item is a file (not a directory)')
			# Determine file type
			FileNameWOExt, FileExt = FuncFileAttrib.ExtractFileExt(OriginalFileNameWithPath)
			FileExt = FileExt.lower()
			if (FileExt == "jpg" or FileExt == "jpeg" or FileExt == "bmp" or FileExt == "png" or FileExt == "gif" or FileExt == "mp4"):
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
	logging.info("****************************************************")
	logging.info('Program Finished')
	logging.info("%d total objects" % Count)
	logging.info("%d files were updated" % ModifiedCount)
	logging.info("%d skipped because they are directories" % DirCount)
	logging.info("%d skipped because they are already properly named" % Already)
	logging.info("%d skipped because they are not a picture" % SkipCount)
	logging.info("****************************************************")

		
# CREATE GUI ROOT DISPLAY
# The following code will define the GUI layout and content
# ************************************************************************************************************
try:
	import tkinter as Tk
	logging.info('Tkinter imported as "tkinter"')
except ImportError:
	import Tkinter as Tk
	logging.info('Tkinter imported as "Tkinter"')
root = Tk.Tk()
root.title('Picture Auto-Renaming App')
minX = maxX = 502
minY = maxY = 610
root.minsize(minX,minY)
root.maxsize(maxX,maxY)
logging.info('%d x %d window created' % (minX, minY))


# CREATE TOP FRAME
# The top-most frame contains a description of the application and instructions for its use
# ************************************************************************************************************
f1w = 500
f1h = 180
f1x = 2
f1y = 2
frame1 = Tk.Frame(root, borderwidth=2, relief=Tk.GROOVE)
frame1.place(anchor=Tk.NW, height=f1h, width=f1w, x=f1x, y=f1y)
logging.info('%d x %d frame created at location (%d, %d)' % (f1h, f1w, f1x, f1y))
text1 = Tk.Message(frame1, anchor=Tk.NW, justify=Tk.CENTER, text="FILE AUTO-NAME APP", width=(f1w-10))
text1.pack(side=Tk.TOP, fill=Tk.X, padx=10, pady=2)
text2 = Tk.Message(frame1, anchor=Tk.NW, justify=Tk.LEFT, text="This application searches a directory structure for files of type PNG, JPG, BMP, or GIF and verifies their filenames comply with a specific naming convention", width=(f1w-10))
text2.pack(side=Tk.TOP, fill=Tk.X, padx=2, pady=2)
text3 = Tk.Message(frame1, anchor=Tk.NW, justify=Tk.LEFT, text="If the filenames do not meet the proper format, the file is automatically renamed to meet the desired format", width=(f1w-10))
text3.pack(side=Tk.TOP, fill=Tk.X, padx=2, pady=2)
text4 = Tk.Message(frame1, anchor=Tk.NW, justify=Tk.LEFT, text="The directory to scan is a user-entered variable", width=(f1w-10))
text4.pack(side=Tk.TOP, fill=Tk.X, padx=2, pady=2)

# CREATE MIDDLE FRAME
# The middle frame contains the data entry field and the "Start" button that triggers the application
# ************************************************************************************************************
f2w = 500
f2h = 100
f2x = 2
f2y = 184
frame2 = Tk.Frame(root, borderwidth=2, relief=Tk.GROOVE)
frame2.place(anchor=Tk.NW, height=f2h, width=f2w, x=f2x, y=f2y)
logging.info('%d x %d frame created at location (%d, %d)' % (f2h, f2w, f2x, f2y))

path = str()
e1 = Tk.Entry(frame2, justify=Tk.LEFT, textvariable=path, width=60)
e1.pack(side=Tk.LEFT, padx=10, pady=10)
e1.delete(0, Tk.END)
e1.insert(0, "c:/exampleDir")
logging.info('Path entry field created in frame 2')

b2 = Tk.Button(frame2,text="Run with current path", height=2, width=10, wraplength=70, command=callback_b1)
b2.pack(side=Tk.RIGHT, padx=10, pady=10)
logging.info('Run button created in frame 2')


# CREATE BOTTOM FRAME
# The bottom-most frame contains status text as the application runs so the user knows what's going on
# ************************************************************************************************************
f3w = 500
f3h = 400
f3x = 2
f3y = 286
frame3 = Tk.Frame(root, borderwidth=2, relief=Tk.GROOVE)
frame3.place(anchor=Tk.NW, height=f3h, width=f3w, x=f3x, y=f3y)
logging.info('%d x %d frame created at location (%d, %d)' % (f3h, f3w, f3x, f3y))


# ENTER TKINTER MAINLOOP
# Entering the mainloop allows the Tkinter code to continuously monitor the status of the GUI widgets
# and act accordingly based upon input
# ************************************************************************************************************
root.mainloop()


