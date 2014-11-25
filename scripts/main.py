__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import os, sys
import autofilename


#######################################################################################################################
# Determine project path and auto-set debug log file and gui configuration file names as appropriate
#######################################################################################################################
#project_path = os.path.split(os.path.abspath(__file__))
project_path = os.path.split(sys.argv[0])
debug_log_file = os.path.normcase(os.path.join(project_path[0], 'debug.log'))
gui_ini_file = os.path.normcase(os.path.join(project_path[0], 'gui_setup.ini'))


#######################################################################################################################
# Start program logger / debugger
#######################################################################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debug_log_file,
                    filemode='w')
logging.info('[Main] Program Logger Started')
logging.info('[Main] Logging to file: %s' % debug_log_file)
logging.info('[Main] Using GUI configuration file: %s' % gui_ini_file)


#######################################################################################################################
# Define Data types
#######################################################################################################################
class ApplicationIO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]


#######################################################################################################################
# Define Data tags used for interlocking between application window and IO monitor threads
#######################################################################################################################
io_table = ApplicationIO()
io_table_cache = ApplicationIO()
io_table_os = ApplicationIO()


#######################################################################################################################
# Start IO monitor thread
#######################################################################################################################
gui_object = autofilename.gui_builder.gui(gui_ini_file, debug_log_file, io_table_os)

IoThread = autofilename.IO_thread.monitor_io(io_table, io_table_cache, io_table_os, debug_log_file, gui_object)
logging.info('[Main] Spawning IO monitor thread (thread-2)')

IoThread.daemon = True
logging.info('[Main] IoThread daemon flag set to "True"')

IoThread.start()
logging.info('[Main] IoThread started')


#######################################################################################################################
# Start application window (runs in main thread)
#######################################################################################################################
gui_object.create_window()
