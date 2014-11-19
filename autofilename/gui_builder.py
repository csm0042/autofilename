import logging
import gui_callbacks
import tkinter as tk



#######################################################################################################################
# Define Helper functions
#######################################################################################################################
def CountWidgetByType(iniFile, searchString):
    import configparser
    Config = configparser.ConfigParser()
    Config.read(iniFile)

    # Initialize counter
    Count = 0

    # Count each of the various types of entries in the INI file
    for section in Config.sections():
        foundPointer = section.find(searchString)
        if foundPointer != -1:
            Count = Count + 1
        pass
    pass
    # Return results
    return Count




#######################################################################################################################
# Define GUI class
#######################################################################################################################
class gui(object):
    def __init__(self, inifile, logfile, iotable):
        self.inifile = inifile
        self.logfile = logfile
        self.iotable = iotable
        self.field = int()
        self.address = int()
        self.text_to_write = str()
        self.text_to_write_mem = str()
        self.place_settings = Place()

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[gui.__init__] Appwindow object created')

        self.root = tk.Tk()
        self.section = str()
        self.Window = Window()

        self.frameCount = CountWidgetByType(self.inifile, "frame")
        self.Frame = Frame()
        self.frame_settings = Frame()
        self.FramePlace = Place()
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]
        logging.info('[gui.__init__] Found configuration data for %d "frame" widgets' %self.frameCount)

        self.messageCount = CountWidgetByType(self.inifile, "message")
        self.Message = Message()
        self.message_settings = Message()
        self.MessagePlace = Place()
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]
        logging.info('[gui.__init__] Found configuration data for %d "message" widgets' %self.messageCount)

        self.textCount = CountWidgetByType(self.inifile, "text")
        self.Text = Text()
        self.text_settings = Text()
        self.TextPlace = Place()
        self.tkText = [tk.Text() for i in range(self.textCount)]
        self.tkTextHandshake = [str() for i in range(self.textCount)]
        logging.info('[gui.__init__] Found configuration data for %d "text" widgets' %self.textCount)

        self.buttonCount = CountWidgetByType(self.inifile, "button")
        self.Button = Button()
        self.button_settings = Button()
        self.ButtonPlace = Place()
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]
        self.ButtonInput = [bool() for i in range(self.buttonCount)]
        logging.info('[gui.__init__] Found configuration data for %d "button" widgets' %self.buttonCount)



    def create_window(self):

        ################################################################################################################
        # CREATE TKINTER MAIN WINDOW
        ################################################################################################################
        self.Window.section = "main window"
        self.Window.iniFile = self.inifile
        self.Window = Window.read_settings(self.Window)
        logging.info('[gui.create_window] Adjusting window geometry')
        self.root.geometry("%sx%s+%s+%s" % (int(self.Window.width), int(self.Window.height), int(self.Window.posX),
                                            int(self.Window.posY)))
        logging.info('[gui.create_window] Adjusting window background color')
        if self.Window.backgroundColor != "":
            self.root.config(background=self.Window.backgroundColor)
        logging.info('[gui.create_window] Setting window title')
        if self.Window.title != '':
            self.root.title(self.Window.title)


        ################################################################################################################
        # CALL LOOP TO CREATE FRAME WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "frame" widget loop')
        for i in range(0, self.frameCount):
            self.Frame.iniFile = self.FramePlace.iniFile = self.inifile
            self.Frame.section = self.FramePlace.section = str("frame" + str(i+1))
            self.Frame.read_settings()
            self.FramePlace.read_settings()
            logging.info('[gui.create_window] Creating frame widget #%d' % (i+1))
            self.tkFrame[i] = self.create_frame_widget(self.tkFrame[i], self.Frame, self.FramePlace)


        ################################################################################################################
        # CALL LOOP TO CREATE MESSAGE WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "message" widget loop')
        for i in range(0, self.messageCount):
            self.Message.iniFile = self.MessagePlace.iniFile = self.inifile
            self.Message.section = self.MessagePlace.section = "message" + str(i+1)
            self.Message.read_settings()
            self.MessagePlace.read_settings()
            logging.info('[gui.create_window] Creating message widget #%d' % (i+1))
            self.tkMessage[i] = self.create_message_widget(self.tkMessage[i], self.Message, self.MessagePlace)


        ################################################################################################################
        # CALL LOOP TO CREATE TEXT WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "text" widget loop')
        for i in range(0, self.textCount):
            self.Text.iniFile = self.TextPlace.iniFile = self.inifile
            self.Text.section = self.TextPlace.section = str("text" + str(i+1))
            self.Text.read_settings()
            self.TextPlace.read_settings()
            logging.info('[gui.create_window] Creating text widget #%d' % (i+1))
            self.tkText[i] = self.create_text_widget(self.tkText[i], self.Text, self.TextPlace)


        ################################################################################################################
        # CALL LOOP TO CREATE BUTTON WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "button" widget loop')
        for i in range(0, self.buttonCount):
            self.Button.iniFile = self.ButtonPlace.iniFile = self.inifile
            self.Button.section = self.ButtonPlace.section = "button" + str(i+1)
            self.Button.read_settings()
            self.ButtonPlace.read_settings()
            logging.info('[gui.create_window] Creating button widget #%d' % (i+1))
            self.tkButton[i] = self.create_button_widget(self.tkButton[i], self.Button, self.ButtonPlace)

        logging.info('[gui.create_window] Starting tkinter main loop')
        self.root.mainloop()
        return self



    def create_frame_widget(self, frame, frame_settings, place_settings):
        self.frame = frame
        self.frame_settings = frame_settings
        self.place_settings = place_settings
        if self.frame_settings.backgroundColor != '':
            self.frame.config(background=self.frame_settings.backgroundColor)
        if self.frame_settings.borderwidth != '':
            self.frame.config(borderwidth=int(self.frame_settings.borderwidth))
        if self.frame_settings.colormap != '':
            self.frame.config(colormap=self.frame_settings.colormap)
        if self.frame_settings.container != '':
            self.frame.config(container=self.frame_settings.container)
        if self.frame_settings.cursor != '':
            self.frame.config(cursor=self.frame_settings.cursor)
        if self.frame_settings.height != '':
            self.frame.config(height=int(self.frame_settings.height))
        if self.frame_settings.highlightBackgroundColor != '':
            self.frame.config(highlightbackground=self.frame_settings.highlightBackgroundColor)
        if self.frame_settings.highlightColor != '':
            self.frame.config(highlightcolor=self.frame_settings.highlightColor)
        if self.frame_settings.highlightThickness != '':
            self.frame.config(highlightthickness=int(self.frame_settings.highlightThickness))
        if self.frame_settings.padX != '':
            self.frame.config(padx=int(self.frame_settings.padX))
        if self.frame_settings.padY != '':
            self.frame.config(pady=int(self.frame_settings.padY))
        if self.frame_settings.relief != '':
            self.frame.config(relief=self.frame_settings.relief)
        if self.frame_settings.takeFocus != '':
            self.frame.config(takefocus=self.frame_settings.takeFocus)
        if self.frame_settings.visual != '':
            self.frame.config(visual=self.frame_settings.visual)
        if self.frame_settings.width != '':
            self.frame.config(width=int(self.frame_settings.width))
        self.frame.place()
        if self.place_settings.anchor != '':
            self.frame.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.frame.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.frame.place_configure(height=int(self.place_settings.height))
        if self.place_settings.width != '':
            self.frame.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relHeight != '':
            self.frame.place_configure(relheight=float(self.place_settings.relHeight))
        if self.place_settings.relWidth != '':
            self.frame.place_configure(relwidth=float(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.frame.place_configure(relx=float(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.frame.place_configure(rely=float(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.frame.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.frame.place_configure(y=int(self.place_settings.offsetY))
        return self.frame


    def create_message_widget(self, message, message_settings, place_settings):
        self.message = message
        self.message_settings = message_settings
        self.place_settings = place_settings
        if self.message_settings.anchor != "":
            self.message.config(anchor=self.message_settings.anchor)
        if self.message_settings.aspect != "":
            self.message.config(aspect=self.message_settings.aspect)
        if self.message_settings.backgroundColor != "":
            self.message.config(background=self.message_settings.backgroundColor)
        if self.message_settings.borderwidth != "":
            self.message.config(borderwidth=self.message_settings.borderwidth)
        if self.message_settings.cursor != "":
            self.message.config(cursor=self.message_settings.cursor)
        if self.message_settings.font != "" and self.message_settings.fontSize != "":
            self.message.config(font=(self.message_settings.font, int(self.message_settings.fontSize)))
        if self.message_settings.foregroundColor != "":
            self.message.config(foreground=self.message_settings.foregroundColor)
        if self.message_settings.highlightBackground != "":
            self.message.config(highlightbackground=self.message_settings.highlightBackground)
        if self.message_settings.highlightBackgroundColor != "":
            self.message.config(highlightcolor=self.message_settings.highlightBackgroundColor)
        if self.message_settings.highlightThickness != "":
            self.message.config(highlightthickness=int(self.message_settings.highlightThickness))
        if self.message_settings.justify != "":
            self.message.config(justify=self.message_settings.justify)
        if self.message_settings.padX != "":
            self.message.config(padx=int(self.message_settings.padX))
        if self.message_settings.padY != "":
            self.message.config(pady=int(self.message_settings.padY))
        if self.message_settings.relief != "":
            self.message.config(relief=self.message_settings.relief)
        if self.message_settings.takeFocus != "":
            self.message.config(takefocus=self.message_settings.takeFocus)
        if self.message_settings.text != "":
            self.message.config(text=self.message_settings.text)
        if self.message_settings.textVariable != "":
            self.message.config(textvariable=self.message_settings.textVariable)
        if self.message_settings.width != "":
            self.message.config(width=int(self.message_settings.width))
        self.message.place()
        if self.place_settings.anchor != '':
            self.message.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.message.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.message.place_configure(height=int(self.place_settings.height))
        if self.place_settings.relHeight != '':
            self.message.place_configure(relheight=int(self.place_settings.relHeight))
        if self.place_settings.width != '':
            self.message.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relWidth != '':
            self.message.place_configure(relwidth=int(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.message.place_configure(relx=int(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.message.place_configure(rely=int(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.message.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.message.place_configure(y=int(self.place_settings.offsetY))
        return self.message


    def create_text_widget(self, text, text_settings, place_settings):
        self.text = text
        self.text_settings = text_settings
        self.place_settings = place_settings
        if self.text_settings.autoSeparators != "":
            self.text.config(autoseparators=self.text_settings.autoSeparators)
        if self.text_settings.backgroundColor != "":
            self.text.config(bg=self.text_settings.backgroundColor)
        if self.text_settings.backgroundStipple != "":
            self.text.config(bgstipple=self.text_settings.backgroundStipple)
        if self.text_settings.borderwidth != "":
            self.text.config(bd=int(self.text_settings.borderwidth))
        if self.text_settings.foregroundStipple != "":
            self.text.config(fgstipple=self.text_settings.foregroundStipple)
        if self.text_settings.cursor != "":
            self.text.config(cursor=self.text_settings.cursor)
        if self.text_settings.exportSelection != "":
            self.text.config(exportselection=self.text_settings.exportSelection)
        if self.text_settings.font != "" and self.text_settings.fontSize != "":
            self.text.config(font=(self.text_settings.font, int(self.text_settings.fontSize)))
        if self.text_settings.foregroundColor != "":
            self.text.config(foreground=self.text_settings.foregroundColor)
        if self.text_settings.foregroundStipple != "":
            self.text.config(fgstipple=self.text_settings.foregroundStipple)
        if self.text_settings.height != "":
            self.text.config(height=int(self.text_settings.height))
        if self.text_settings.highlightBackgroundColor != "":
            self.text.config(highlightbackground=self.text_settings.highlightBackgroundColor)
        if self.text_settings.highlightColor != "":
            self.text.config(highlightcolor=self.text_settings.highlightColor)
        if self.text_settings.highlightThickness != "":
            self.text.config(highlightthickness=int(self.text_settings.highlightThickness))
        if self.text_settings.insertBackground != "":
            self.text.config(insertbackground=self.text_settings.insertBackground)
        if self.text_settings.insertBorderwidth != "":
            self.text.config(insertBorderwidth=int(self.text_settings.insertBorderwidth))
        if self.text_settings.insertOffTime != "":
            self.text.config(insertOffTime=int(self.text_settings.insertOffTime))
        if self.text_settings.insertOnTime != "":
            self.text.config(insertOnTime=int(self.text_settings.insertOnTime))
        if self.text_settings.insertWidth != "":
            self.text.config(insertWidth=int(self.text_settings.insertWidth))
        if self.text_settings.lmargin1 != "":
            self.text.config(lmargin1=int(self.text_settings.lmargin1))
        if self.text_settings.lmargin2 != "":
            self.text.config(lmargin2=int(self.text_settings.lmargin2))
        if self.text_settings.maxUndo != "":
            self.text.config(maxundo=int(self.text_settings.maxUndo))
        if self.text_settings.padX != "":
            self.text.config(padx=int(self.text_settings.padX))
        if self.text_settings.padY != "":
            self.text.config(pady=int(self.text_settings.padY))
        if self.text_settings.offset != "":
            self.text.config(offset=int(self.text_settings.offset))
        if self.text_settings.overstrike != "":
            self.text.config(overstrike=self.text_settings.overstrike)
        if self.text_settings.relief != "":
            self.text.config(offset=self.text_settings.relief)
        if self.text_settings.rmargin != "":
            self.text.config(overstrike=int(self.text_settings.rmargin))
        if self.text_settings.selectBackgroundColor != "":
            self.text.config(selectbackground=self.text_settings.selectBackgroundColor)
        if self.text_settings.selectForegroundColor != "":
            self.text.config(selectforeground=self.text_settings.selectForegroundColor)
        if self.text_settings.selectBorderwidth != "":
            self.text.config(selectborderwidth=int(self.text_settings.selectBorderwidth))
        if self.text_settings.setGrid != "":
            self.text.config(setgrid=self.text_settings.SetGrid)
        if self.text_settings.spacing1 != "":
            self.text.config(spacing1=int(self.text_settings.spacing1))
        if self.text_settings.spacing2 != "":
            self.text.config(spacing2=int(self.text_settings.spacing2))
        if self.text_settings.spacing3 != "":
            self.text.config(spacing3=int(self.text_settings.spacing3))
        if self.text_settings.state != "":
            self.text.config(state=self.text_settings.state)
        if self.text_settings.tabs != "":
            self.text.config(tabs=self.text_settings.tabs)
        if self.text_settings.takeFocus != "":
            self.text.config(takefocus=self.text_settings.takeFocus)
        if self.text_settings.text != "":
            self.text.insert(tk.END, self.text_settings.text)
        if self.text_settings.underline != "":
            self.text.config(underline=self.text_settings.underline)
        if self.text_settings.undo != "":
            self.text.config(undo=int(self.text_settings.undo))
        if self.text_settings.width != "":
            self.text.config(width=int(self.text_settings.width))
        if self.text_settings.wrap != "":
            self.text.config(wrap=self.text_settings.wrap)
        if self.text_settings.xScrollCommand != "":
            self.text.config(xscrollcommand=int(self.text_settings.xScrollCommand))
        if self.text_settings.yScrollCommand != "":
            self.text.config(yscrollcommand=int(self.text_settings.yScrollCommand))
        self.text.place()
        if self.place_settings.anchor != '':
            self.text.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.text.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.text.place_configure(height=int(self.place_settings.height))
        if self.place_settings.relHeight != '':
            self.text.place_configure(relheight=int(self.place_settings.relHeight))
        if self.place_settings.width != '':
            self.text.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relWidth != '':
            self.text.place_configure(relwidth=int(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.text.place_configure(relx=int(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.text.place_configure(rely=int(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.text.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.text.place_configure(y=int(self.place_settings.offsetY))
        return self.text
    

    def create_button_widget(self, button, button_settings, place_settings):
        self.button = button
        self.button_settings = button_settings
        self.place_settings = place_settings
        if self.button_settings.backgroundColor != '':
            self.button.config(background=self.button_settings.backgroundColor)
        if self.button_settings.bitmap != '':
            self.button.config(bitmap=self.button_settings.bitmap)
        if self.button_settings.borderwidth != '':
            self.button.config(borderwidth=int(self.button_settings.borderwidth))
        if self.button_settings.command != '':
            self.button.config(command=lambda instance=int(self.button_settings.command):
            gui_callbacks.callback(self, instance, self.logfile))
        if self.button_settings.compound != '':
            self.button.config(compound=self.button_settings.compound)
        if self.button_settings.cursor != '':
            self.button.config(cursor=self.button_settings.cursor)
        if self.button_settings.default != '':
            self.button.config(default=self.button_settings.default)
        if self.button_settings.disableForeground != '':
            self.button.config(disableforeground=self.button_settings.disableForeground)
        if self.button_settings.font != '' and self.button_settings.fontSize != '':
            self.button.config(font=(self.button_settings.font, int(self.button_settings.fontSize)))
        if self.button_settings.foregroundColor != '':
            self.button.config(foreground=self.button_settings.foregroundColor)
        if self.button_settings.height != '':
            self.button.config(height=int(self.button_settings.height))
        if self.button_settings.highlightBackgroundColor != '':
            self.button.config(highlightbackground=self.button_settings.highlightBackgroundColor)
        if self.button_settings.highlightColor != '':
            self.button.config(highlightcolor=self.button_settings.highlightColor)
        if self.button_settings.highlightThickness != '':
            self.button.config(highlightthickness=int(self.button_settings.highlightThickness))
        if self.button_settings.image != '':
            self.button.config(image=self.button_settings.image)
        if self.button_settings.justify != '':
            self.button.config(justify=self.button_settings.justify)
        if self.button_settings.overRelief != '':
            self.button.config(overrelief=self.button_settings.overRelief)
        if self.button_settings.padX != '':
            self.button.config(padx=int(self.button_settings.padX))
        if self.button_settings.padY != '':
            self.button.config(pady=int(self.button_settings.padY))
        if self.button_settings.relief != '':
            self.button.config(relief=self.button_settings.relief)
        if self.button_settings.repeatDelay != '':
            self.button.config(repeatdelay=int(self.button_settings.repeatDelay))
        if self.button_settings.repeatInterval != '':
            self.button.config(repeatinterval=int(self.button_settings.repeatInterval))
        if self.button_settings.state != '':
            self.button.config(state=self.button_settings.state)
        if self.button_settings.takeFocus != '':
            self.button.config(takefocus=self.button_settings.takeFocus)
        if self.button_settings.text != '':
            self.button.config(text=self.button_settings.text)
        if self.button_settings.textVariable != '':
            self.button.config(textvariable=self.button_settings.textVariable)
        if self.button_settings.underline != '':
            self.button.config(underline=self.button_settings.underline)
        if self.button_settings.width != '':
            self.button.config(width=int(self.button_settings.width))
        if self.button_settings.wrapLength != '':
            self.button.config(wraplength=int(self.button_settings.wrapLength))
        self.button.place()            
        if self.place_settings.anchor != '':
            self.button.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.button.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.button.place_configure(height=int(self.place_settings.height))
        if self.place_settings.width != '':
            self.button.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relHeight != '':
            self.button.place_configure(relheight=int(self.place_settings.relHeight))
        if self.place_settings.relWidth != '':
            self.button.place_configure(relwidth=int(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.button.place_configure(relx=int(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.button.place_configure(rely=int(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.button.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.button.place_configure(y=int(self.place_settings.offsetY))
        return self.button




    ####################################################################################################################
    # Define interface methods for GUI class
    ####################################################################################################################
    def return_root(self):
        logging.info('[gui.return_root] Returning window object')
        return self.root

    def kill_root(self):
        logging.info('[gui.kill_root] Killing root window process')
        self.root.destroy()
        return

    def return_text(self, field):
        self.field = field
        self.address = self.field - 1
        logging.info('[gui.return_text] Returning text from text field #%d' % self.field)
        return self.tkText[self.address].get("1.0", tk.END)

    def write_text(self, field, text_to_write):
        self.field = field
        self.address = self.field - 1
        self.text_to_write = text_to_write
        if self.text_to_write != self.text_to_write_mem:
            self.tkText[self.address].insert(tk.END, self.text_to_write)
            #logging.info('[gui.write_text] Writing text to text field #%d' % self.field)
            self.text_to_write_mem = self.text_to_write
        return

    def clear_text(self, field):
        self.field = field
        self.address = self.field - 1
        self.tkText[self.address].delete(1.0, tk.END)
        logging.info('[gui.clear_text] Clearing text to text field #%d' % self.field)
        return




#######################################################################################################################
# Define Window class
#######################################################################################################################
class Window(object):
    def __init__(self):
        self.width = str()
        self.height = str()
        self.posX = str()
        self.posY = str()
        self.title = str()
        self.backgroundColor = str()
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.width = dict1['width']
        self.height = dict1['height']
        self.posX = dict1['pos x']
        self.posY = dict1['pos y']
        self.title = dict1['title']
        self.backgroundColor = dict1['background color']

        return self




#######################################################################################################################
# Define Frame widget class
#######################################################################################################################
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
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.backgroundColor = dict1['background color']
        self.borderwidth = dict1['border width']
        self.colormap = dict1['color map']
        self.container = dict1['container']
        self.cursor = dict1['cursor']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.takeFocus = dict1['take focus']
        self.visual = dict1['visual']
        self.width = dict1['width']

        return self




#######################################################################################################################
# Define Message widget class
#######################################################################################################################
class Message(object):
    def __init__(self):
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
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.anchor = dict1['anchor']
        self.aspect = dict1['aspect']
        self.backgroundColor = dict1['background color']
        self.borderwidth = dict1['border width']
        self.cursor = dict1['cursor']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.highlightBackground = dict1['highlight background']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightThickness = dict1['highlight thickness']
        self.justify = dict1['justify']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.textVariable = dict1['text variable']
        self.width = dict1['width']

        return self




#######################################################################################################################
# Define Text widget class
#######################################################################################################################
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
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.autoSeparators = dict1['auto separators']
        self.backgroundColor = dict1['background color']
        self.backgroundStipple = dict1['background stipple']
        self.borderwidth = dict1['border width']
        self.cursor = dict1['cursor']
        self.exportSelection = dict1['export selection']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.foregroundStipple = dict1['foreground stipple']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.insertBackground = dict1['insert background']
        self.insertBorderwidth = dict1['insert border width']
        self.insertOffTime = dict1['insert off time']
        self.insertOnTime = dict1['insert on time']
        self.insertWidth = dict1['insert width']
        self.justify = dict1['justify']
        self.lmargin1 = dict1['lmargin1']
        self.lmargin2 = dict1['lmargin2']
        self.maxUndo = dict1['max undo']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.offset = dict1['offset']
        self.overstrike = dict1['overstrike']
        self.relief = dict1['relief']
        self.rmargin = dict1['rmargin']
        self.selectBackgroundColor =dict1['select background color']
        self.selectForegroundColor = dict1['select foreground color']
        self.selectBorderwidth = dict1['select border width']
        self.setGrid = dict1['set grid']
        self.spacing1 = dict1['spacing1']
        self.spacing2 = dict1['spacing2']
        self.spacing3 = dict1['spacing3']
        self.state = dict1['state']
        self.tabs = dict1['tabs']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.underline = dict1['underline']
        self.undo = dict1['undo']
        self.width = dict1['width']
        self.wrap = dict1['wrap']
        self.xScrollCommand = dict1['x scroll command']
        self.yScrollCommand = dict1['y scroll command']

        return self




#######################################################################################################################
# Define Button widget class
#######################################################################################################################
class Button(object):
    def __init__(self):
        self.activeBackgroundColor = str()
        self.activeForegroundColor = str()
        self.anchor = str()
        self.backgroundColor = str()
        self.bitmap = str()
        self.borderwidth = int()
        self.command = int()
        self.compound = str()
        self.cursor = str()
        self.default = str()
        self.disableForeground = str()
        self.font = str()
        self.fontSize = int()
        self.foregroundColor = str()
        self.height = int()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = int()
        self.image = str()
        self.justify = str()
        self.overRelief = str()
        self.padX = int()
        self.padY = int()
        self.relief = str()
        self.repeatDelay = int()
        self.repeatInterval = int()
        self.state = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.underline = str()
        self.width = int()
        self.wrapLength = int()
        self.iniFile = str()
        self.section = str()


    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.backgroundColor = dict1['background color']
        self.bitmap = dict1['bitmap']
        self.borderwidth = dict1['border width']
        self.command = dict1['command']
        self.compound = dict1['compound']
        self.cursor = dict1['cursor']
        self.default = dict1['default']
        self.disableForeground = dict1['disable foreground']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.image = dict1['image']
        self.justify = dict1['justify']
        self.overRelief = dict1['over relief']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.repeatDelay = dict1['repeat delay']
        self.repeatInterval = dict1['repeat interval']
        self.state = dict1['state']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.textVariable = dict1['text variable']
        self.underline = dict1['underline']
        self.width = dict1['width']
        self.wrapLength = dict1['wrap length']

        return self




#######################################################################################################################
# Define place settings class
#######################################################################################################################
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
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.anchor = dict1['place anchor']
        self.borderMode = dict1['place border mode']
        self.height = dict1['place height']
        self.width = dict1['place width']
        self.relHeight = dict1['place rel height']
        self.relWidth = dict1['place rel width']
        self.relX = dict1['place rel x']
        self.relY = dict1['place rel y']
        self.offsetX = dict1['place offset x']
        self.offsetY = dict1['place offset y']

        return self




########################################################################################################################
#  Run if script is called manually
########################################################################################################################
if __name__ == "__main__":
    ioTable = int()
    AppWindowObject = gui('gui_setup.ini', 'debug.log', ioTable)
    app = AppWindowObject.create_window()