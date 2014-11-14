__author__ = 'chris.maue'

import SpawnGuiFromIni

def callback(Appwindow, instance):
    if instance == 1:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF1 Pressed')
        pass

    if instance == 2:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF2 Pressed')
        pass

    if instance == 3:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF3 Pressed')
        pass

    if instance == 4:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF4 Pressed')
        pass

    if instance == 5:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF5 Pressed')
        pass

    if instance == 6:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF6 Pressed')
        pass

    if instance == 7:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF7 Pressed')
        pass

    if instance == 8:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF8 Pressed')
        pass

    if instance == 9:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF9 Pressed')
        pass

    if instance == 10:
        SpawnGuiFromIni.SpawnAppwindow.write_text(Appwindow, 0, '\nF10 Pressed')
        pass

    if instance == 11:
        SpawnGuiFromIni.SpawnAppwindow.clear_text(Appwindow, 0)
        pass
    if instance == 12:
        text = SpawnGuiFromIni.SpawnAppwindow.return_text(Appwindow, 0)
        print(text)
        pass

    if instance == 13:
        Appwindow.root.destroy()
        pass

