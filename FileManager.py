#File Manager Class for File Handling (Creating and Autofilling content in files.)

import os
import common_GUI_functions as cGUIf #short-hand
from tkinter import filedialog


#Custom functions for file handling
def writelines_infile(filename,lines):
    """Writelines in the specific file"""

    with open(filename,"w") as file:
        file.writelines(lines)

def create_file(filename):
    """Creates an empty file."""

    open(filename,"x").close()

def read_n_return(filename):
    """Reads and returns the content of a file."""

    with open(filename,"r") as file:
        all_content = file.read()

    return all_content

def paste_content(filename,content):
    """Pastes all content in a file."""

    #Check if file already exists and empty
    if os.path.exists(filename) and os.stat(filename).st_size == 0:
        
        with open(filename,"w") as file:
            
            file.write(content)    

class FileManager(object):
    """Creates and Autofills Files."""

    #Dict that relates file names with their extensions

    NAMES_N_EXTS = {
        "HTML"   : ".html",
        "CSS"    : ".css",
        "JS"     : ".js",
        "Python" : ".py",
        "Java"   : ".java"
        }

    #Dict that relates file names with their autofilled content (if any)
    NAMES_N_AUTOCONTENT = {
        "HTML"   :   ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "  <head> \n\n"
                                "      <meta charset=\"UTF-8\"> \n\n",
                                "      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "      <title>Default Title</title> \n\n",
                                "  </head> \n\n",
                                "  <body> \n",
                                "  </body> \n\n",
                                "</html>"],
        
        "CSS"    :   ["/*Base Styling*/\n\n",
                                        "* \n",
                                        "{ \n",
                                        "    box-sizing: border-box; \n",
                                        "} \n\n\n\n",
                                        "/*Mobile Devices Styling*/\n\n",
                                        "@media (min-width: 320px) and (max-width: 479px) \n",
                                        "{} \n\n\n\n",
                                        "/*Tablet Devices Styling*/\n\n",
                                        "@media (min-width: 480px) and (max-width: 959px) \n",
                                        "{} \n\n\n\n",
                                        "/*Desktop Devices Styling*/\n\n",
                                        "@media (min-width: 960px) \n",
                                        "{}"],

        "Python"  :  ["\n\n\n\n",
                           "def main(): \n",
                           "    pass \n",
                           "\n\n\n\n",
                           "if __name__ == \"__main__\": \n",
                           "    main()"]

        }

    def __init__(self,name,location,file_type, further_choice):
        """Initialize this FileManager object."""

        #Attributes for the file to create.
        self.name = name
        self.location = location
        self.file_type = file_type
        self.further_choice = further_choice

        #Define file extension
        self.ext = FileManager.NAMES_N_EXTS[self.file_type]

        #Define the name of the file with its extension
        self.name_extended = self.name + self.ext

        #Define the whole name of the file
        self.whole_name = os.path.join(self.location,self.name_extended)

        #Success status of procedures
        self.created = True
        self.autofilled = True
        self.pasted = True

        #Functions to run each time an instance is generated
        self.generate_file() #First create the file

        #If file was generated succesfully, then it's possible to run further operations
        if self.created:
            #Autofill file if the user asked for it
            if self.further_choice == "Autofill":
                self.autofill_file()

            elif self.further_choice == "None":
                #Do nothing
                pass

            else:
                #Paste content from another file of the same type
                self.paste_from()

            #If there was any mistake, delete the generated file
            if not self.autofilled or not self.pasted:
                self.delete_file()

            #If not say all operations were succesful
            else:
                cGUIf.show_info("Success Pop-Up",
                                "All operations were successful.")

    def generate_file(self):
        """Generates the file of the required type."""

        try:
            create_file(self.whole_name)

        except FileExistsError:
            cGUIf.show_error("Creation Error",
                             f"The file {self.name_extended}" \
                             + f"\nalready exists in {self.location}")
            
            self.created = False

        except OSError as oserror:
            cGUIf.show_error("Creation Error",
                             "An error related to the Operating System happend." \
                             + "\n\nTo be more specific:" \
                             + f"\n{oserror}")

            self.created = False

    def autofill_file(self):
        """Autofill file if it's possible."""

        #Check if file can be autofilled
        if self.file_type in FileManager.NAMES_N_AUTOCONTENT:

            try:
                #Get the autocontent and write it in the file
                writelines_infile(self.whole_name,
                                  FileManager.NAMES_N_AUTOCONTENT[self.file_type])

            except OSError as oserror:
                cGUIf.show_error("Autofill Error",
                                 "An errror related to the Operating System happened." \
                                 + "\n\nTo be more specific:" \
                                 + f"\n{oserror}")
                
                self.autofilled = False

        #If not tell the user there's no way to autofill that file
        else:
            cGUIf.show_warning("Autofilling Warning",
                               f"Sorry, but file of type {self.file_type}" \
                               + " cannot be autofilled by this programme.")

    def paste_from(self):
        """Paste content from another file in the created file."""

        #Ask for a reader file
        reader_file = filedialog.askopenfilename(title = f"Select a {self.file_type} reader file.",
                                                 filetypes = [(f"{self.file_type} Files",
                                                               f"*{FileManager.NAMES_N_EXTS[self.file_type]}")])

        #Ensure user does not select an empty file
        if os.stat(reader_file).st_size == 0:
            cGUIf.show_error("Pasting Error",
                             "Cannot copy content from empty file.")

        else:
            #Execute the process as usual
            try:
                le_content = read_n_return(reader_file)
                paste_content(self.whole_name,le_content)

            except UnicodeDecodeError as e:
                cGUIf.show_error("Pasting Error",
                                 "An encoding decoding error happened." \
                                 + "\n\nTo be more specific:" \
                                 + f"\n{e}")
                
                self.pasted = False

            except OSError as oserror:
                cGUIf.show_error("Pasting Error",
                                 "An error related to the Operating System happened." \
                                 + "\n\nTo be more specific: " \
                                 + "f\n{oserror}")

                self.pasted = False
                
    def delete_file(self):
        """Run if file was created but an error happened in a further operation."""
        os.remove(self.whole_name)
        cGUIf.show_warning("Deletion Warning",
                        f"The file {self.whole_name} was permanently deleted from your system.")

if __name__ == "__main__": 

    #Tell User this programme is not meant to be run directly
    cGUIf.show_warning("Import Warning",
                 "This module contains a Project Manager Class for the\n" \
                 + "\"File Generator\" programme." \
                 + "\n\nThis module IS NOT MEANT TO BE RUN DIRECTLY." \
                 + "\nPlease, IMPORT IT IN ANOTHER SCRIPT.")
