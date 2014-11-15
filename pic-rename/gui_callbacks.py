__author__ = 'chris.maue'

#import file_rename
from file_rename import FileRename
import logging
import sys
sys.path.insert(0, 'c:/python34/MyProjects/gui-by-ini/guibyini')
import SpawnGuiFromIni


def callback(AppWindowObject, instance, logfile):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                        filename=logfile, filemode='w')
    logging.info('[gui_callbacks] called with a value of %d' % instance)

    if instance == 1:
        AppWindowObject.root.destroy()
        pass

    if instance == 2:
        path = SpawnGuiFromIni.AppWindow.return_text(AppWindowObject, 1)
        SpawnGuiFromIni.AppWindow.clear_text(AppWindowObject, 2)
        SpawnGuiFromIni.AppWindow.write_text(AppWindowObject, 1, ('\nUsing path --> ' + str(path)))
        fileRenameObject = FileRename(str(path), logfile)
        fileRenameObject.RunLoop()

        pass

