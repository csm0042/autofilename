__author__ = 'chris.maue'


import logging
import rename_script


def callback(AppWindowObject, instance, logfile):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                        filename=logfile, filemode='w')
    logging.info('[gui_callbacks] called with a value of %d' % instance)

    if instance == 1:
        AppWindowObject.root.destroy()
        pass

    if instance == 2:
        path = str(AppWindowObject.return_text(1))
        AppWindowObject.clear_text(2)
        AppWindowObject.write_text(2, ('\nUsing path --> ' + str(path)))
        rename_script.rename_script(str(path), logfile)


