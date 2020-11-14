#         Main GUI Tkinter of the File Generator Programme GUI Version

#Imports
from tkinter import *
from tkinter import filedialog
from tkinter import font
import common_GUI_functions as cGUIf
import Little_Top

#Create MainFrame class

class MainFrame(Frame):
    """Main Frame of the File Generator Programme."""

    def __init__(self, master, width, height, font_families, images_paths):
        """Instantiate this Frame."""

        #Call parent's constructor method
        super(MainFrame, self).__init__(master,
                                        width = width,
                                        height = height)

        #Define the fonts for this frame
        self.font_sizes = (30,13,13) #Sizes for fonts
        self.fonts = [] #List of all fonts

        for family, size in zip(font_families,self.font_sizes):
            self.fonts.append(font.Font(family = family, size = size))


        #Convert fonts list to tuple to not change it
        self.fonts = tuple(self.fonts)

        #Save all images in a list of images
        self.images = []

        for image_path in images_paths:
            self.images.append(cGUIf.get_TkImage(image_path,64,64))

        #Convert image list to tuple to not change it
        self.images = tuple(self.images)
        
        #Record how many times user asked for folder location
        self.times_asked_folder = 0

        #Show all widgets right away
        self.show_widgets()

    def show_widgets(self):
        """Defines and shows all default widgets of this Frame."""

        #A Label for the title of the programme

        self.title = cGUIf.get_TextLabel(self,
                                   "Automatic File Generator",
                                   self.fonts[0],
                                   160,
                                   50)

        #A Label for the subtitle
        self.subtitle = cGUIf.get_TextLabel(self,
                                      "Creates and/or autofills standalone files",
                                      self.fonts[2],
                                      245,
                                      120)

        #A Label for File Information

        self.file_info = cGUIf.get_TextLabel(self,
                                       "File Info",
                                       self.fonts[1],
                                       325,
                                       160)

        #A Label for File Name
        self.file_name = cGUIf.get_TextLabel(self,
                                       "Name:",
                                       self.fonts[1],
                                       30,
                                       220)

        #Entry widget for File Name
        self.enter_name = cGUIf.get_Entry(self,self.fonts[2],90,220)

        #A Label for File Location
        self.file_location = cGUIf.get_TextLabel(self,
                                           "Location:",
                                           self.fonts[1],
                                           325,
                                           220)

        #Entry widget for File Location
        self.enter_location = cGUIf.get_Entry(self,self.fonts[2],427,220)

        #Button to invoke filedialog
        self.location_bttn = cGUIf.get_Button(self,
                                        "Browse",
                                        self.browse_machine,
                                        650,
                                        220)

        #Label for file types
        self.file_types = cGUIf.get_TextLabel(self,
                                        "Types",
                                        self.fonts[1],
                                        340,
                                        280)

        #Generate labels for Files
        self.html_label = cGUIf.get_TextLabel(self,
                                        "HTML",
                                        "",
                                        90,
                                        340)

        self.css_label = cGUIf.get_TextLabel(self,
                                       "CSS",
                                       "",
                                       353,
                                       340)

        self.js_label = cGUIf.get_TextLabel(self,
                                      "JS",
                                      "",
                                      620,
                                      340)


        self.python_label = cGUIf.get_TextLabel(self,
                                          "Python",
                                          "",
                                          200,
                                          470)

        self.java_label = cGUIf.get_TextLabel(self,
                                        "Java",
                                        "",
                                        500,
                                        470)

        #Create Image Labels for Files
        self.html_pic = cGUIf.get_ImgLabel(self,
                                           self.images[0],
                                           75,
                                           385)
        
        self.css_pic = cGUIf.get_ImgLabel(self,
                                          self.images[1],
                                          335,
                                          385)

        self.js_pic = cGUIf.get_ImgLabel(self,
                                         self.images[2],
                                         595,
                                         385)

        self.python_pic = cGUIf.get_ImgLabel(self,
                                             self.images[3],
                                             187,
                                             505)

        self.java_pic = cGUIf.get_ImgLabel(self,
                                           self.images[4],
                                           477,
                                           505)

        #Radiobuttons to indicate which file to create
        self.file_type = StringVar(self)
        self.file_type.set("Python")

        self.possible_options = ("HTML", "CSS", "JS", "Python", "Java") #Tuple of possible file choices

        #HTML Radiobutton
        self.html_radiob = cGUIf.get_Radiobutton(self,
                                                 "",
                                                 self.file_type,
                                                 self.possible_options[0],
                                                 self.change_bttn_txt,
                                                 98,
                                                 465)

        #CSS Radiobutton
        self.css_radiob = cGUIf.get_Radiobutton(self,
                                               "",
                                               self.file_type,
                                               self.possible_options[1],
                                               self.change_bttn_txt,
                                               358,
                                               465)

        #JS Radiobutton
        self.js_radiob = cGUIf.get_Radiobutton(self,
                                               "",
                                               self.file_type,
                                               self.possible_options[2],
                                               self.change_bttn_txt,
                                               620,
                                               465)

        #Python Radiobutton
        self.python_radiob = cGUIf.get_Radiobutton(self,
                                                   "",
                                                   self.file_type,
                                                   self.possible_options[3],
                                                   self.change_bttn_txt,
                                                   210,
                                                   585)

        #Java Radiobutton
        self.java_radiob = cGUIf.get_Radiobutton(self,
                                                 "",
                                                 self.file_type,
                                                 self.possible_options[4],
                                                 self.change_bttn_txt,
                                                 500,
                                                 585)
        #Button to create file
        self.create_file_bttn = cGUIf.get_Button(self,
                                                 f"Create {self.file_type.get()} File",
                                                 self.ask_further_option,
                                                 635,
                                                 615) #Specify file type

    def browse_machine(self):
        """Browses machine file system for a folder path."""

        #Ask for a directory
        self.folder = filedialog.askdirectory()

        #Increase the times the user pressed the button
        self.times_asked_folder += 1

        #Delete previous content if any exists
        if self.times_asked_folder > 0:
            self.enter_location.delete(0,END)

        #Add folder path to entry widget when selected
        self.enter_location.insert(0, self.folder)

    def change_bttn_txt(self):
        """Changes the text displayed by the "Create File" Button
        when a radiobutton is clicked."""

        self.create_file_bttn.configure(text = f"Create {self.file_type.get()} File")

    
    def ask_further_option(self):
        """Gives the required info to the File Manager and invokes it
        to execute the appropiate file operations."""

        #Ensure user wrote a name for the file

        if len(self.enter_name.get()) == 0:
            cGUIf.show_warning("Creation Warning", "Cannot create file " \
                               + "whose name is empty")

        else:
            #Open secondary window to ask for further options
            self.jic = Little_Top.main(
                self.enter_name.get(),
                self.enter_location.get(),
                self.file_type.get()) #Just in case we want to do something
 

#Tell user this module contains a frame class for another programme
#The module should not be run directly
if __name__ == "__main__":
    
    cGUIf.show_warning("Import Warning",
                       "This module contains a frame class for the " \
                       + "\"Automatic File Generator\" programme." \
                       + "\n\nThis module IS NOT MEANT TO BE RUN DIRECTLY." \
                       + "\nPlease, IMPORT IT IN ANOTHER SCRIPT.")
