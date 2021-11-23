from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as Text1 
from tkinter import Menu
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import font , colorchooser, filedialog, messagebox
import os

window=Tk()
window.title('Notepad')
window.geometry('700x600')



global_path = " "
global_title = " "
save_flag = None



scrollbar = Scrollbar(window)
editor = Text(yscrollcommand = scrollbar.set)
scrollbar.pack(side= RIGHT, fill= Y)
scrollbar.config(command= editor.yview)
editor.pack(fill= 'both', expand= True)




def newFile(event= 'n'):
    window.title("Untitled - Notepad")
    file=None
    editor.delete(1.0,END)

def openFile(event= 'o'):
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.**"),("text document","*.txt")])
    if file=="":
        file=None
    else:
        window.title(os.path.basename(file)+" -Notepad")
        editor.delete(1.0,END)
        file=open(file,"r")
        editor.insert(1.0,file.read())
        file.close()


def saveAs():
    global global_path
    global global_title

    save_file_path = asksaveasfilename(initialfile="Untitle.txt",
                                       defaultextension=".txt",
                                       filetypes= [('Any File', '*.txt, *.py....')])
    with open(save_file_path, 'w') as file:
        text = editor.get('1.0', END)
        file.write(text)
    # Updating the global variables.
    global_path = save_file_path
    window.title(os.path.basename(save_file_path)+" - Notepade")
    global_title = save_file_path

# Save Function.
def save(event= 's'):
    global save_flag 
    global global_title

    save_flag = True
    text = editor.get('1.0', END)
    # If it's a new file go to save as else save it in the existing file.
    if global_path == ' ':
        saveAs()
    else:
        with open(global_path, 'w') as file:
            file.write(text)

    window.title(os.path.basename(global_path)+" - Notepade")
    global_title = global_path
    

def Print(event = 'p'):
    if global_path == " ":
        showerror('Error', 'Please save the file before printing !!')
    else:
        os.startfile(global_path, 'print')
        

def cutFile(event = 'x'):
    editor.event_generate("<<Cut>>")

def copyFile(event = 'c'):
    editor.event_generate("<<Copy>>")

def pasteFile(event = 'v'):
    editor.event_generate("<<Paste>>")

def Exit():
    if save_flag==None and editor.get(0.0,END)!="\n":
        userinput=askquestion("File not saved.","Do you want to save this file?")
    if userinput=='yes':
        saveAs()
    window.quit()




    


def timesNewRoman():
    editor.configure(font=("times New Roman", 20, "italic"))
  
def Lucida():
        editor.configure(font=("lucida 25"))
def Algerian():
    editor.configure(font=("ALGERIAN", 20, "bold"))
def ARIAL():
    editor.configure(font=("Arial", 20, "bold"))
def Calibri():
    editor.configure(font=("Calibri", 20))
def MS_Outlook():
      editor.configure(font=("MS Outlook", 20 ))
def Impact():
         editor.configure(font=("Impact", 20))
def modern():
    editor.configure(font=("Modern", 20))
def highTowerText():
    editor.configure(font=("High Tower Text", 20))
def Harrington():
       editor.configure(font=("Harrington", 20))


def font():
    window=Tk()
    window.title('FONT WINDOW')
    window.geometry('700x600')

    lbl=Label(window,text="*****THIS IS FONT SELECTION PAGE*****",font=('times new roman',20))
    lbl.grid(column=0,row=0)
    lbl=Label(window,text='PLEASE SELECT THE FONT',font=('times new roman',20))
    lbl.grid(column=0,row=1)
    btn=Button(window,text='Times new roman',command=timesNewRoman,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=3)
    btn=Button(window,text='lucida 20',command=Lucida, bg='white',font=('times new roman',20))
    btn.grid(column=0, row=4)
    btn=Button(window,text='ALGERIAN',command=Algerian,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=5)
    btn=Button(window,text='Arial',command=ARIAL,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=6)
    btn=Button(window,text='Calibri',command=Calibri,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=7)
    btn=Button(window,text='MS Outlook',command=MS_Outlook,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=8)
    btn=Button(window,text='Impact',command=Impact,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=9)
    btn=Button(window,text='Modern',command=modern,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=10)
    btn=Button(window,text='High Tower Text',command=highTowerText,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=11)
    btn=Button(window,text='Harrington',command=Harrington,bg='white',font=('times new roman',20))
    btn.grid(column=0, row=12)
    

    

    


def Run(event = 'F5'):
    if global_path == " ":
        showerror('Error', 'Please save your file first !!')
    else:
        if '.py' in global_path:
            code = editor.get('1.0', END) 
            exec(code)
        else:
            showerror('Error', 'This is not a valid Python File !!')
    


def viewHelp():
    showinfo("Notepad","How do I change header and footer commands in Notepad?\nHow do I use Notepad to create a log?\nHow do I use XML Notepad to create an XML document?\nTo open Notepad,select the Start Windows logo Start button and then type Notepad in the search box.\nSelect Notepad from the results.\nIf you need additional help, ask the Microsoft Community.")

def sendFeed():
    showinfo("Your FeedBack","Successfully")


def feedBack():
    window=Tk()
    window.title('FeedBack Hub')
    window.geometry('700x500')
    lbl=Label(window,text='Enter Your FeedBack',font=('times new roman',20))
    lbl.grid(column=0,row=0)
    lbl=Label(window,text='Summarize Your FeedBack',font=('times new roman',15))
    lbl.grid(column=0,row=1)
    ent=Entry(window,width=50)
    ent.grid(column=0,row=2)
    lbl=Label(window,text='Explain in more detail(Optional)',font=('times new roman',15))
    lbl.grid(column=0,row=3)
    ent=Entry(window,width=50)
    ent.grid(column=0,row=4)
    btn=Button(window,text='Send',command=sendFeed,bg='Green',font=('times new roman',25))
    btn.grid(column=0, row=6)
  
def aboutDevelopers():
    showinfo("Notepad","This app is developed by Group 1 and Group 2 member\n1.Dejene Tolera\n2.Getu Niguse\n3.Dendea Terakegn\n4.Gemmechu Iyasu\n5.Negussie Duba\n6.Dheresa Amante")

def showAbout():
    showinfo("Notepad","Notepad is a simple text editor for Microsoft Windows and a basic text-editing program which enables computer users to create documents.")
             
menubar = Menu(window)

filemenu=Menu(menubar,tearoff=0)
editmenu=Menu(menubar,tearoff=0)
formatmenu=Menu(menubar,tearoff=0)
runmenu=Menu(menubar,tearoff=0)
viewmenu=Menu(menubar,tearoff=0)
helpmenu=Menu(menubar,tearoff=0)
zoomsubmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label="New                 Ctrl+N", command=newFile)
filemenu.add_command(label="Open               Ctrl+O", command=openFile)
filemenu.add_command(label="Save                 Ctrl+S", command=save)
filemenu.add_command(label="Save as  Ctrl+Shift+S", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Print                Ctrl+P", command=Print)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_cascade(label='Cut            Ctrl+X', command=cutFile)
editmenu.add_cascade(label='Copy         Ctrl+C', command=copyFile)
editmenu.add_cascade(label='Paste         Ctrl+V', command=pasteFile)
editmenu.add_separator()
editmenu.add_cascade(label='Exit', command=Exit)

menubar.add_cascade(label='Format',menu=formatmenu)
formatmenu.add_cascade(label='Font', command=font)
formatmenu.add_separator()
formatmenu.add_cascade(label='Exit', command=Exit)

menubar.add_cascade(label='Run',menu=runmenu)
runmenu.add_cascade(label='Run         F5',command=Run)

menubar.add_cascade(label='View', menu=viewmenu)
viewmenu.add_cascade(label='Zoom', menu=zoomsubmenu)
zoomsubmenu.add_cascade(label='Zoom In')
zoomsubmenu.add_cascade(label='Zoom Out')
viewmenu.add_separator()
viewmenu.add_cascade(label='Exit', command=Exit)


menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_cascade(label='View Help', command=viewHelp)
helpmenu.add_cascade(label='Send Feedback', command=feedBack)
helpmenu.add_cascade(label='About Developer',command=aboutDevelopers)
helpmenu.add_cascade(label='About This App',command=showAbout)

window.config(menu=menubar)
# Shortcut Key bindings.
window.bind('<Control-n>', newFile )
window.bind('<Control-o>', openFile)
window.bind('<Control-s>', save)
window.bind('<Control-Shift-s>', saveAs)
window.bind('<Control-p>', Print)
window.bind('<Control-x>', cutFile)
window.bind('<Control-c>', copyFile)
window.bind('<Control-v>', pasteFile)
window.bind('<F5>', Run)

window.mainloop()
