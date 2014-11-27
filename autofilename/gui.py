# ###############################################################################################################
#IMPORT LIBRARIES
################################################################################################################
import logging
import tkinter as tk
import autofilename


################################################################################################################
#DEFINE CLASS
################################################################################################################
class Window(object):
    def __init__(self):
        self.width = str()
        self.height = str()
        self.posX = str()
        self.posY = str()
        self.title = str()
        self.backgroundColor = str()
        self.title = str()


class Frame(object):
    def __init__(self):
        self.backgroundColor = str()
        self.borderwidth = str()
        self.colormap = str()
        self.container = str()
        self.cursor = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.takeFocus = str()
        self.visual = str()
        self.width = str()


class Message(object):
    def __init__(self):
        self.anchor = str()
        self.anchor = str()
        self.aspect = str()
        self.backgroundColor = str()
        self.borderwidth = str()
        self.cursor = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.highlightBackground = str()
        self.highlightBackgroundColor = str()
        self.highlightThickness = str()
        self.justify = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.width = str()


class Text(object):
    def __init__(self):
        self.autoSeparators = str()
        self.backgroundColor = str()
        self.backgroundStipple = str()
        self.borderwidth = str()
        self.cursor = str()
        self.exportSelection = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.foregroundStipple = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.insertBackground = str()
        self.insertBorderwidth = str()
        self.insertOffTime = str()
        self.insertOnTime = str()
        self.insertWidth = str()
        self.justify = str()
        self.lmargin1 = str()
        self.lmargin2 = str()
        self.maxUndo = str()
        self.padX = str()
        self.padY = str()
        self.offset = str()
        self.overstrike = str()
        self.relief = str()
        self.rmargin = str()
        self.selectBackgroundColor = str()
        self.selectForegroundColor = str()
        self.selectBorderwidth = str()
        self.setGrid = str()
        self.spacing1 = str()
        self.spacing2 = str()
        self.spacing3 = str()
        self.state = str()
        self.tabs = str()
        self.takeFocus = str()
        self.text = str()
        self.underline = str()
        self.undo = str()
        self.width = str()
        self.wrap = str()
        self.xScrollCommand = str()
        self.yScrollCommand = str()


class Button(object):
    def __init__(self):
        self.activeBackgroundColor = str()
        self.activeForegroundColor = str()
        self.anchor = str()
        self.backgroundColor = str()
        self.bitmap = str()
        self.borderwidth = str()
        self.command = str()
        self.compound = str()
        self.cursor = str()
        self.default = str()
        self.disableForeground = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.image = str()
        self.justify = str()
        self.overRelief = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.repeatDelay = str()
        self.repeatInterval = str()
        self.state = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.underline = str()
        self.width = str()
        self.wrapLength = str()


class Place(object):
    def __init__(self):
        self.anchor = str()
        self.borderMode = str()
        self.height = str()
        self.width = str()
        self.relHeight = str()
        self.relWidth = str()
        self.relX = str()
        self.relY = str()
        self.offsetX = str()
        self.offsetY = str()


################################################################################################################
#DEFINE GUI CLASS
################################################################################################################
class gui(object):
    def __init__(self, logfile):
        self.logfile = logfile
        self.root = tk.Tk()

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[gui.__init__] Appwindow object created')

        self.frameCount = 3
        self.Frame = Frame()
        self.frame_settings = Frame()
        self.FramePlace = Place()
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]
        logging.info('[gui.__init__] Found configuration data for %d frame widgets' % self.frameCount)

        self.messageCount = 4
        self.Message = Message()
        self.message_settings = Message()
        self.MessagePlace = Place()
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]
        logging.info('[gui.__init__] Found configuration data for %d message widgets' % self.messageCount)

        self.textCount = 4
        self.Text = Text()
        self.text_settings = Text()
        self.TextPlace = Place()
        self.text_to_write = str()
        self.text_to_write_mem = str()
        self.tkText = [tk.Text() for i in range(self.textCount)]
        logging.info('[gui.__init__] Found configuration data for %d text widgets' % self.textCount)

        self.buttonCount = 2
        self.Button = Button()
        self.button_settings = Button()
        self.ButtonPlace = Place()
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]
        logging.info('[gui.__init__] Found configuration data for %d button widgets' % self.buttonCount)


    ################################################################################################################
    #CREATE TKINTER MAIN WINDOW
    ################################################################################################################
    def create_window(self):
        logging.info('[gui.create_window] Adjusting window geometry')
        self.root.geometry("%sx%s+%s+%s" % (500, 610, 10, 10))
        self.root.config(background='gray')
        logging.info('[gui.create_window] Adjusting window background color')
        self.root.title('File Auto-Rename')
        logging.info('[gui.create_window] Setting window title')

        logging.info('[gui.create_window] Starting frame widget loop')
        logging.info('[gui.create_window] Creating frame widget #%d' % 1)
        self.tkFrame[0] = tk.Frame()
        self.tkFrame[0].config(borderwidth=2)
        self.tkFrame[0].config(height=90)
        self.tkFrame[0].config(relief='sunken')
        self.tkFrame[0].config(width=496)
        self.tkFrame[0].place()
        self.tkFrame[0].place_configure(anchor='nw')
        self.tkFrame[0].place_configure(bordermode='inside')
        self.tkFrame[0].place_configure(x=2)
        self.tkFrame[0].place_configure(y=2)

        logging.info('[gui.create_window] Creating frame widget #%d' % 2)
        self.tkFrame[1] = tk.Frame()
        self.tkFrame[1].config(borderwidth=2)
        self.tkFrame[1].config(height=105)
        self.tkFrame[1].config(relief='sunken')
        self.tkFrame[1].config(width=496)
        self.tkFrame[1].place()
        self.tkFrame[1].place_configure(anchor='nw')
        self.tkFrame[1].place_configure(bordermode='inside')
        self.tkFrame[1].place_configure(x=2)
        self.tkFrame[1].place_configure(y=94)

        logging.info('[gui.create_window] Creating frame widget #%d' % 3)
        self.tkFrame[2] = tk.Frame()
        self.tkFrame[2].config(borderwidth=2)
        self.tkFrame[2].config(height=392)
        self.tkFrame[2].config(relief='sunken')
        self.tkFrame[2].config(width=496)
        self.tkFrame[2].place()
        self.tkFrame[2].place_configure(anchor='nw')
        self.tkFrame[2].place_configure(bordermode='inside')
        self.tkFrame[2].place_configure(x=2)
        self.tkFrame[2].place_configure(y=203)

        logging.info('[gui.create_window] Starting message widget loop')
        logging.info('[gui.create_window] Creating message widget #%d' % 1)
        self.tkMessage[0] = tk.Message()
        self.tkMessage[0].config(anchor='nw')
        self.tkMessage[0].config(font=('Aerial', 8))
        self.tkMessage[0].config(foreground='black')
        self.tkMessage[0].config(highlightthickness=1)
        self.tkMessage[0].config(
            text='This application searches a directory structure for files of type PNG, JPG, BMP, or GIF and verifies their filenames comply with a specific naming convention.  If the filenames do not meet the proper format, the file is automatically renamed to meet the desired format.  The directory to scan is a user-entered variable.')
        self.tkMessage[0].config(width=410)
        self.tkMessage[0].place()
        self.tkMessage[0].place_configure(anchor='nw')
        self.tkMessage[0].place_configure(bordermode='inside')
        self.tkMessage[0].place_configure(height=60)
        self.tkMessage[0].place_configure(width=410)
        self.tkMessage[0].place_configure(x=10)
        self.tkMessage[0].place_configure(y=10)

        logging.info('[gui.create_window] Creating message widget #%d' % 2)
        self.tkMessage[1] = tk.Message()
        self.tkMessage[1].config(anchor='nw')
        self.tkMessage[1].config(font=('Aerial', 8))
        self.tkMessage[1].config(foreground='black')
        self.tkMessage[1].config(highlightthickness=1)
        self.tkMessage[1].config(text='Root directory to scan:')
        self.tkMessage[1].config(width=150)
        self.tkMessage[1].place()
        self.tkMessage[1].place_configure(anchor='nw')
        self.tkMessage[1].place_configure(bordermode='inside')
        self.tkMessage[1].place_configure(height=20)
        self.tkMessage[1].place_configure(width=150)
        self.tkMessage[1].place_configure(x=5)
        self.tkMessage[1].place_configure(y=107)

        logging.info('[gui.create_window] Creating message widget #%d' % 3)
        self.tkMessage[2] = tk.Message()
        self.tkMessage[2].config(anchor='nw')
        self.tkMessage[2].config(font=('Aerial', 8))
        self.tkMessage[2].config(foreground='black')
        self.tkMessage[2].config(highlightthickness=1)
        self.tkMessage[2].config(text='File-types to include:')
        self.tkMessage[2].config(width=150)
        self.tkMessage[2].place()
        self.tkMessage[2].place_configure(anchor='nw')
        self.tkMessage[2].place_configure(bordermode='inside')
        self.tkMessage[2].place_configure(height=20)
        self.tkMessage[2].place_configure(width=150)
        self.tkMessage[2].place_configure(x=5)
        self.tkMessage[2].place_configure(y=137)

        logging.info('[gui.create_window] Creating message widget #%d' % 4)
        self.tkMessage[3] = tk.Message()
        self.tkMessage[3].config(anchor='nw')
        self.tkMessage[3].config(font=('Aerial', 8))
        self.tkMessage[3].config(foreground='black')
        self.tkMessage[3].config(highlightthickness=1)
        self.tkMessage[3].config(text='Include sub-folders?:')
        self.tkMessage[3].config(width=150)
        self.tkMessage[3].place()
        self.tkMessage[3].place_configure(anchor='nw')
        self.tkMessage[3].place_configure(bordermode='inside')
        self.tkMessage[3].place_configure(height=20)
        self.tkMessage[3].place_configure(width=150)
        self.tkMessage[3].place_configure(x=5)
        self.tkMessage[3].place_configure(y=167)

        logging.info('[gui.create_window] Starting text widget loop')
        logging.info('[gui.create_window] Creating text widget #%d' % 1)
        self.tkText[0] = tk.Text()
        self.tkText[0].config(bg='white')
        self.tkText[0].config(bd=2)
        self.tkText[0].config(font=('Aerial', 8))
        self.tkText[0].config(foreground='black')
        self.tkText[0].config(height=28)
        self.tkText[0].config(padx=5)
        self.tkText[0].config(pady=5)
        self.tkText[0].config(state='normal')
        self.tkText[0].insert(tk.END, "C:\\Users\\cmaue\\OneDrive\\Pictures\\_New")
        self.tkText[0].config(width=362)
        self.tkText[0].config(wrap='word')
        self.tkText[0].place()
        self.tkText[0].place_configure(anchor='nw')
        self.tkText[0].place_configure(bordermode='inside')
        self.tkText[0].place_configure(height=28)
        self.tkText[0].place_configure(width=362)
        self.tkText[0].place_configure(x=130)
        self.tkText[0].place_configure(y=105)

        logging.info('[gui.create_window] Creating text widget #%d' % 2)
        self.tkText[1] = tk.Text()
        self.tkText[1].config(bg='black')
        self.tkText[1].config(bd=2)
        self.tkText[1].config(font=('Aerial', 8))
        self.tkText[1].config(foreground='white')
        self.tkText[1].config(height=370)
        self.tkText[1].config(padx=5)
        self.tkText[1].config(pady=5)
        self.tkText[1].config(state='normal')
        self.tkText[1].config(width=480)
        self.tkText[1].config(wrap='word')
        self.tkText[1].place()
        self.tkText[1].place_configure(anchor='nw')
        self.tkText[1].place_configure(bordermode='inside')
        self.tkText[1].place_configure(height=380)
        self.tkText[1].place_configure(width=480)
        self.tkText[1].place_configure(x=10)
        self.tkText[1].place_configure(y=210)

        logging.info('[gui.create_window] Creating text widget #%d' % 3)
        self.tkText[2] = tk.Text()
        self.tkText[2].config(bg='white')
        self.tkText[2].config(bd=2)
        self.tkText[2].config(font=('Aerial', 8))
        self.tkText[2].config(foreground='black')
        self.tkText[2].config(height=28)
        self.tkText[2].config(padx=5)
        self.tkText[2].config(pady=5)
        self.tkText[2].config(state='normal')
        self.tkText[2].insert(tk.END, "jpg, bmp, gif, png, jpeg, flv, mp4, webm")
        self.tkText[2].config(width=362)
        self.tkText[2].config(wrap='word')
        self.tkText[2].place()
        self.tkText[2].place_configure(anchor='nw')
        self.tkText[2].place_configure(bordermode='inside')
        self.tkText[2].place_configure(height=28)
        self.tkText[2].place_configure(width=305)
        self.tkText[2].place_configure(x=130)
        self.tkText[2].place_configure(y=135)

        logging.info('[gui.create_window] Creating text widget #%d' % 4)
        self.tkText[3] = tk.Text()
        self.tkText[3].config(bg='white')
        self.tkText[3].config(bd=2)
        self.tkText[3].config(font=('Aerial', 8))
        self.tkText[3].config(foreground='black')
        self.tkText[3].config(height=28)
        self.tkText[3].config(padx=5)
        self.tkText[3].config(pady=5)
        self.tkText[3].config(state='normal')
        self.tkText[3].insert(tk.END, "yes")
        self.tkText[3].config(width=100)
        self.tkText[3].config(wrap='word')
        self.tkText[3].place()
        self.tkText[3].place_configure(anchor='nw')
        self.tkText[3].place_configure(bordermode='inside')
        self.tkText[3].place_configure(height=28)
        self.tkText[3].place_configure(width=100)
        self.tkText[3].place_configure(x=130)
        self.tkText[3].place_configure(y=165)

        logging.info('[gui.create_window] Starting button widget loop')
        logging.info('[gui.create_window] Creating button widget #%d' % 1)
        self.tkButton[0] = tk.Button()
        self.tkButton[0].config(background='red')
        self.tkButton[0].config(borderwidth='2')
        self.tkButton[0].config(command=lambda instance=1: gui.callback(self, instance))
        self.tkButton[0].config(font=('Aerial', 12))
        self.tkButton[0].config(height=28)
        self.tkButton[0].config(justify='center')
        self.tkButton[0].config(text='X')
        self.tkButton[0].config(width=28)
        self.tkButton[0].config(wraplength='28')
        self.tkButton[0].place()
        self.tkButton[0].place_configure(anchor='ne')
        self.tkButton[0].place_configure(bordermode='inside')
        self.tkButton[0].place_configure(height=28)
        self.tkButton[0].place_configure(width=28)
        self.tkButton[0].place_configure(x=492)
        self.tkButton[0].place_configure(y=15)

        logging.info('[gui.create_window] Creating button widget #%d' % 2)
        self.tkButton[1] = tk.Button()
        self.tkButton[1].config(background='gray')
        self.tkButton[1].config(borderwidth='2')
        self.tkButton[1].config(command=lambda instance=2: gui.callback(self, instance))
        self.tkButton[1].config(font=('Aerial', 8))
        self.tkButton[1].config(height=50)
        self.tkButton[1].config(justify='center')
        self.tkButton[1].config(text='Rename Files')
        self.tkButton[1].config(width=50)
        self.tkButton[1].config(wraplength='45')
        self.tkButton[1].place()
        self.tkButton[1].place_configure(anchor='ne')
        self.tkButton[1].place_configure(bordermode='inside')
        self.tkButton[1].place_configure(height=50)
        self.tkButton[1].place_configure(width=50)
        self.tkButton[1].place_configure(x=492)
        self.tkButton[1].place_configure(y=140)

        self.root.mainloop()


    def callback(self, instance):
        self.instance = instance

        if self.instance == 1:
            logging.info('[gui.callback] Button %d pressed' % 1)
            gui.kill_root(self)

        if self.instance == 2:
            logging.info('[gui.callback] Button %d pressed' % 2)
            path = str(gui.return_text(self, 1))
            types = str(gui.return_text(self, 3))
            include = str(gui.return_text(self, 4))
            gui.clear_text(self, 2)
            gui.write_text(self, 2, ('\nUsing path --> ' + str(path)))
            autofilename.rename_script(str(path), self.logfile, types, include)


    def return_root(self):
        return self.root


    def kill_root(self):
        self.root.destroy()
        return


    def return_text(self, field):
        self.field = field
        self.address = self.field - 1
        return self.tkText[self.address].get("1.0", tk.END)


    def write_text(self, field, text_to_write):
        self.field = field
        self.address = self.field - 1
        self.text_to_write = text_to_write
        if self.text_to_write != self.text_to_write_mem:
            self.tkText[self.address].insert(tk.END, self.text_to_write)
            self.text_to_write_mem = self.text_to_write
        return


    def clear_text(self, field):
        self.field = field
        self.address = self.field - 1
        self.tkText[self.address].delete("1.0", tk.END)
        return


if __name__ == "__main__":
    appwindow = gui('debug.log')
    appwindow.create_window()