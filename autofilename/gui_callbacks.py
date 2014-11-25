__author__ = 'chris.maue'


import logging
from .rename_script import *


def callback(gui_object, instance, logfile):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                        filename=logfile, filemode='w')
    logging.info('[gui_callbacks] called with a value of %d' % instance)

    if instance == 1:
        gui_object.root.destroy()
        pass

    if instance == 2:
        path = str(gui_object.return_text(1))
        types = str(gui_object.return_text(3))
        include = str(gui_object.return_text(4))
        gui_object.clear_text(2)
        gui_object.write_text(2, ('\nUsing path --> ' + str(path)))
        rename_script(str(path), logfile, types, include)

