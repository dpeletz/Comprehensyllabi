# Jack Freier and David Peletz

# -------------------------------------------------------------------------------------------------

# This file contains a GUI for importing and parsing a .pdf syllabus. The intended functionality is
# to first import the desired file, and then extract its relevant information.

# -------------------------------------------------------------------------------------------------
# Import Statements:

from tkinter import *
import easygui
import pdf_extraction

# -------------------------------------------------------------------------------------------------
# Global Variables:

root_win = None
parsed_text = None

# -------------------------------------------------------------------------------------------------
# GUI Main Function Definition:

def GUIMain():
    """Main function for the program. Creates a Graphical User Interface and assigns commands to specific
    elements of it. Has no parameters and returns nothing."""

    global root_win

    root_win = Tk()
    root_win.title("Comprehensyllabi")
    root_win.configure(bg="#7AC5CD")


    titleLabel = Label(root_win, text="Comprehensyllabi", bg="#7AC5CD", fg="gray1", padx=40, pady=5,
                       font="Verdana 18 bold")
    titleLabel.grid(row=0, column=0)

    label1 = Label(root_win, text="Import and parse\nyour syllabus:", bg="#7AC5CD", fg="gray1", padx=5, pady=5,
                   font="Verdana 12 bold italic")
    label1.grid(row=1, column=0)

    label2 = Label(root_win, text="", bg="#7AC5CD", fg="#7AC5CD", padx=5, pady=0,
                   font="Verdana 12 bold italic")
    label2.grid(row=3, column=0)

    import_button = Button(root_win, text="Import", width=7, bg="#EEE8CD", fg="black", activeforeground="#2F4F4F", bd=3,
                          font="Verdana 12 bold", relief=RIDGE, overrelief=SUNKEN, command=import_file)
    import_button.grid(row=2, column=0)

    quit_button = Button(root_win, text="Quit", width=7, bg="#EEE8CD", fg="#CD0000", activeforeground="#FF0000", bd=3,
                        font="Verdana 12 bold", relief=RIDGE, overrelief=SUNKEN, command=quit)
    quit_button.grid(row=4, column=0)

    root_win.mainloop()

# -------------------------------------------------------------------------------------------------
# Primary Function Definitions:

def import_f():
    """Imports a .pdf file from the user's device. Helper function for the GUI function. Takes no inputs
    and returns a file path in string format."""
    file_path = easygui.fileopenbox(filetypes=['*.pdf'])
    return file_path

def parse_s(file):
    """Parses the syllabus to extract relevant information. Simplifies the .pdf file to contain relevant
    information. Helper function for the GUI function. Takes a string file path as its sole input, returning
    a .csv file."""
    pdf_extraction.get_useful_information(file)



# -------------------------------------------------------------------------------------------------
# GUI Function Definitions:

def import_file():
    """Takes no inputs and returns nothing. Imports the file to be parsed using a helper function."""
    global root_win
    parse_s(import_f())

def quit():
    """Takes no inputs and returns nothing. Upon being called, destroys the GUI."""
    global root_win
    root_win.destroy()

# -------------------------------------------------------------------------------------------------
# GUI Main Function Call:

GUIMain()