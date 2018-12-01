# Jack Freier and David Peletz

# -------------------------------------------------------------------------------------------------

# This file contains a GUI for importing and parsing a .pdf syllabus. The intended functionality is
# to first import the desired file, and then extract its relevant information.

# -------------------------------------------------------------------------------------------------
# Import Statements:

from tkinter import *
import tkinter.messagebox as mBox
import easygui
import pdf_extraction

# -------------------------------------------------------------------------------------------------
# Global Variables:

rootWin = None
parsedText = None

# -------------------------------------------------------------------------------------------------
# GUI Main Function Definition:

def GUIMain():
    """Main function for the program. Creates a Graphical User Interface and assigns commands to specific
    elements of it. Has no parameters and returns nothing."""

    global rootWin
    global parsedText

    rootWin = Tk()
    rootWin.title("Syllabus Information Parser")
    rootWin.configure(bg="#CDC9C9")

    parsedText = StringVar()

    titleLabel = Label(rootWin, text="Syllabus Simplifier", bg="#CDC9C9", fg="gray1", padx=40, pady=5,
                    font="Verdana 18 bold")
    titleLabel.grid(row=0, column=0)

    label1 = Label(rootWin, text="Import your Syllabus:", bg="#CDC9C9", fg="gray1", padx=5, pady=5,
                    font="Verdana 12 bold italic")
    label1.grid(row=1, column=0)

    label2 = Label(rootWin, text="Parse your Syllabus:", bg="#CDC9C9", fg="gray1", padx=5, pady=5,
                    font="Verdana 12 bold italic")
    label2.grid(row=3, column=0)

    label3 = Label(rootWin, text="Parsed Text:", bg="#CDC9C9", fg="gray1", padx=5, pady=5,
                    font="Verdana 12 bold italic")
    label3.grid(row=5, column=0)

    importButton = Button(rootWin, text="Import", width=7, bg="#F5F5F5", fg="black", activeforeground="#2F4F4F", bd=3,
                    font="Verdana 12 bold", relief=RIDGE, overrelief=SUNKEN, command=importFile)
    importButton.grid(row=2, column=0)

    parseButton = Button(rootWin, text="Parse", width=7, bg="#F5F5F5", fg="black", activeforeground="#2F4F4F", bd=3,
                    font="Verdana 12 bold", relief=RIDGE, overrelief=SUNKEN, command=parseSyllabus)
    parseButton.grid(row=4, column=0)

    quitButton = Button(rootWin, text="Quit", width=7, bg="#F5F5F5", fg="#CD0000", activeforeground="#FF0000", bd=3,
                    font="Verdana 12 bold", relief=RIDGE, overrelief=SUNKEN, command=quit)
    quitButton.grid(row=8, column=0)

    txtEntry = Entry(rootWin, textvariable=parsedText, bg="#efefef", fg="black", bd=5, font="Verdana 12",
                     justify=CENTER, relief=SUNKEN, width=20)
    txtEntry.grid(row=6, column=0)

    label4 = Label(rootWin, text="", bg="#CDC9C9", fg="gray1", padx=5, pady=0,
                    font="Verdana 12 bold italic")
    label4.grid(row=7, column=0)

    rootWin.mainloop()

# -------------------------------------------------------------------------------------------------
# Primary Function Definitions:

def importF():
    """Imports a .pdf file from the user's device."""
    filePath = easygui.fileopenbox(filetypes=['*.pdf'])
    return filePath

def parseS():
    """Parses the syllabus to extract relevant information. Simplifies the .pdf file to contain relevant information."""

# -------------------------------------------------------------------------------------------------
# GUI Function Definitions:

def importFile():
    """Takes no inputs and returns nothing. Imports the file to be parsed using a helper function."""
    global rootWin
    importF()

def parseSyllabus():
    """Takes no inputs and returns nothing. Parses the previously imported syllabus using a helper function."""
    global rootWin
    parseS()
    parsedText.set("ass")

def quit():
    """Takes no inputs and returns nothing. Upon being called, destroys the GUI."""
    global rootWin
    rootWin.destroy()

# -------------------------------------------------------------------------------------------------
# GUI Main Function Call:

GUIMain()