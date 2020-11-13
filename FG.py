#                  GUI Version of the File Generator Programme

#It will look way better, it will be way better
#:)

#Imports
import enhancedTk, MainFrame, os

#GLOBAL CONSTANTS

FONT_FAMILIES = ("Arial","Courier New","Times New Roman")#Fonts families for the GUI
PICS_FOLDER = "images" #Name of folder where Images are located
ICON_PATH = os.path.join("images", "iconsin.ico") #Path to app's icon
PICS_PATH = (os.path.join("images", "html.png"),
             os.path.join("images", "css.png"),
             os.path.join("images", "js.png"),
             os.path.join("images", "python.png"),
             os.path.join("images", "java.png")
             )

#Window's proportions
WIDTH = 750
HEIGHT = 650

def main(): 
    """Run the programme."""

    #Create enhancedTk.Super_Tk() window instance
    window = enhancedTk.Super_Tk(title = "AFG",
                                 icon_path = ICON_PATH,
                                 width = WIDTH,
                                 height = HEIGHT)

    #Create MainFrame that contains main programme widgets and interactions
    app_frame = MainFrame.MainFrame(window,
                                    WIDTH,
                                    HEIGHT,
                                    FONT_FAMILIES,
                                    PICS_PATH)

    #Display MainFrame on the screen
    app_frame.place(x = 0, y = 0)

    #Continue to display GUI window
    window.mainloop()


if __name__ == "__main__": 
    main()
