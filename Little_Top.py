#Executes secondary window that asks for further options

#Imports
from tkinter import *
from tkinter import font
import FileManager, MainFrame, enhancedTk, FG
import common_GUI_functions as cGUIf

#GLOBAL CONSTANTS
WIDTH = 500
HEIGHT = 450

def main(name,location,filetype):
    """Runs the whole programme."""

    #Create top level window for the FG programme
    topsin = enhancedTk.Top_Super_Tk(title = "AFG",
                                     icon_path = FG.ICON_PATH,
                                     width = WIDTH,
                                     height = HEIGHT)

    #Instantiate TopFrame and add it to the toplevel window
    topf = TopFrame(topsin,WIDTH,HEIGHT,FG.FONT_FAMILIES,
                    name,location,filetype)
    topf.place(x = 0, y = 0)

    #Keep running top window
    topsin.mainloop()

    #Destroy when Toplevel is closed
    topsin.destroy()

    return topsin, topf
    

    

class TopFrame(Frame):
    """Frame for the further options window."""

    def __init__(self,master,width,height,font_families,
                 name,location,filetype):
        """Initialize this TopFrame."""

        #Call Parent's constructor method
        super(TopFrame, self).__init__(master,
                                       width = width,
                                       height = height)

        #Attributes to be passed to the FileManager
        self.name = name
        self.location = location
        self.filetype = filetype

        #Define fonts for this frame
        self.font_sizes = (20,12,12)
        self.fonts = []

        for family, size in zip(font_families,self.font_sizes):
            self.fonts.append(font.Font(family = family, size = size))

        self.fonts = tuple(self.fonts)

        #Add widgets defined in this frame
        self.add_widgets()

    def add_widgets(self):
        """Adds all default widgets to the frame."""

        #Add text label to tell what's this frame about
        self.title = cGUIf.get_TextLabel(self,
                                         "Further Options",
                                         self.fonts[0],
                                         150,
                                         50)

        #Labels that show info about the file to be created
        self.show_name = cGUIf.get_TextLabel(self,
                                             f"File Name: {self.name}",
                                             self.fonts[1],
                                             180,
                                             110)

        self.show_location = cGUIf.get_TextLabel(self,
                                                 "File Location:",
                                                 self.fonts[1],
                                                 100,
                                                 160)

        self.ent_location = cGUIf.get_Entry(self,
                                            self.fonts[2],
                                            250,
                                            160)

        self.show_filetype = cGUIf.get_TextLabel(self,
                                                 f"File Type: {self.filetype}",
                                                 self.fonts[1],
                                                 180,
                                                 210)
        
        #Modify the entry widget in which the file location will go
        self.ent_location.insert(0, f"{self.location}")
        self.ent_location.configure(state = "readonly")

        #Create Radiobuttons for those options
        self.option = StringVar(self)
        self.option.set("None")

        self.none_radiob = cGUIf.get_Radiobutton(self,
                                                 "None",
                                                 self.option,
                                                 "None",
                                                 "",
                                                 220,
                                                 270)

        self.autofill_radiob = cGUIf.get_Radiobutton(self,
                                                     "Autofill",
                                                     self.option,
                                                     "Autofill",
                                                     "",
                                                     220,
                                                     300)

        self.pasteFrom_radiob = cGUIf.get_Radiobutton(self,
                                                      "Paste Content From...",
                                                      self.option,
                                                      "Paste Content From...",
                                                      "",
                                                      220,
                                                      330)

        #Create Button to Create the File along with the operation selected
        self.final_bttn = cGUIf.get_Button(self,
                                           "Execute Operations",
                                           self.invoke_FileManager,
                                           210,
                                           375)

    def invoke_FileManager(self):
        """Invokes the File Manager Object"""

        le_fm = FileManager.FileManager(self.name,
                                        self.location,
                                        self.filetype,
                                        self.option.get())


#Tell user what this module is about
#And that it should not be run directly.
if __name__ == "__main__":
    cGUIf.show_warning("Import Warning",
                       "This module contains the code that runs the toplevel " \
                       + "window that asks for further options in the Automatic " \
                       + "File Generator Programme." \
                       + "\n\nThis module IS NOT MEANT TO BE RUN DIRECTLY." \
                       + "\nPlease, IMPORT IT IN ANOTHER FILE.")
