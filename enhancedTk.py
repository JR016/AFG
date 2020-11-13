from tkinter import *
from PIL import ImageTk, Image
import sys, os
import common_GUI_functions as cGUIf

class Super_Tk(Tk):
    """A version of tkinter Tk to programme GUI's faster."""

    def __init__(self, title = "", icon_path = "", width = 500, height = 500, is_resizable = False):
        """Initialize GUI window with special attributes."""

        #Call Parent constructor method
        super(Super_Tk, self).__init__()

        #Set new title and icon_path if possible
        if isinstance(title,str):
            if len(title) > 0:
                self.title(title)

        else:
            self.withdraw()
            cGUIf.show_error("TypeError", f'"title" must be of type str, not of type {type(title)}.')
            self.destroy()
            sys.exit(1)
            
        #Set window to not resizable
        if isinstance(is_resizable,bool):
            if not is_resizable:
                self.resizable(False,False)

        else:
            self.withdraw()
            cGUIf.show_error("TypeError", f'"is_resizable" must be of bool type, not of type {type(is_resizable)}.')
            self.destroy()
            sys.exit(1)
        
        #Check if it is possible to apply an Image (Do some error handling)
        if isinstance(icon_path,str):
            if len(icon_path) > 0:
                try:

                    #First check file type of icon
                    self.icon_type = os.path.splitext(icon_path)[-1]

                    if self.icon_type == ".ico":
                        self.iconbitmap(icon_path)
                        
                    else:
                        self.iconphoto(False, PhotoImage(file = icon_path))

                except TclError as tkerror:
                    self.withdraw() #Close window if error occurs
                    cGUIf.show_error("Fatal Error", tkerror)
                    self.destroy()
                    sys.exit(1) #Cancel all operations

        #Set window size if possible (Do some Error handling)

        if width != "" and height != "":
            try:
                self.geometry(f"{width}x{height}")

            except TclError as tkerror:
                self.withdraw()
                cGUIf.show_error("Fatal Error", tkerror)
                self.destroy()
                sys.exit(1)

class Top_Super_Tk(Toplevel):
    
    """Top Level Window based on its parent."""

    
    def __init__(self, title = "", icon_path = "", width = 500, height = 500, is_resizable = False):
        """Initialize GUI window with special attributes."""

        super(Top_Super_Tk, self).__init__()

        #Set new title and icon_path if possible
        if isinstance(title,str):
            if len(title) > 0:
                self.title(title)

        else:
            self.withdraw()
            cGUIf.show_error("TypeError", f'"title" must be of type str, not of type {type(title)}.')
            self.destroy()
            sys.exit(1)
            
        #Set window to not resizable
        if isinstance(is_resizable,bool):
            if not is_resizable:
                self.resizable(False,False)

        else:
            self.withdraw()
            cGUIf.show_error("TypeError", f'"is_resizable" must be of bool type, not of type {type(is_resizable)}.')
            self.destroy()
            sys.exit(1)
        
        #Check if it is possible to apply an Image (Do some error handling)
        if isinstance(icon_path,str):
            if len(icon_path) > 0:
                try:

                    #First check file type of icon
                    self.icon_type = os.path.splitext(icon_path)[-1]

                    if self.icon_type == ".ico":
                        self.iconbitmap(icon_path)
                        
                    else:
                        self.iconphoto(False, PhotoImage(file = icon_path))

                except TclError as tkerror:
                    self.withdraw() #Close window if error occurs
                    cGUIf.show_error("Fatal Error", tkerror)
                    self.destroy()
                    sys.exit(1) #Cancel all operations

        #Set window size if possible (Do some Error handling)

        if width != "" and height != "":
            try:
                self.geometry(f"{width}x{height}")

            except TclError as tkerror:
                self.withdraw()
                cGUIf.show_error("Fatal Error", tkerror)
                self.destroy()
                sys.exit(1)


#Tell the user the program is not meant to be run directly
if __name__ == "__main__":    

    cGUIf.show_warning("Import Warning", "This module containts a modified versions " \
                       + "of Tk()\n(The Tkinter Window Object) and Toplevel() (The Tkinter Secondary Window Object)" \
                       + "\nfor simple and fast GUI projects" \
                       + "\n\nThis module is NOT MEANT TO BE RUN DIRECTLY.\nPlease, IMPORT IT IN ANOTHER SCRIPT.")
