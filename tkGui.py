'''
    Gui stuff with tkinter
'''
from tkinter import *
from tkinter import filedialog as fd 
from tkinter import messagebox as alert

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Apri File", command=self.openFile)
        fileMenu.add_command(label="Apri Cartella", command=self.openDir)
        fileMenu.add_command(label="Mostra messaggio", command=self.showMessage)
        fileMenu.add_command(label="Esci", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        self.pack(fill=BOTH, expand=1)
        
        text = Label(self, text="ZipCycle", font=("Helvetica",14))
        text.place(x=10,y=10)
        #text.pack()


    def exitProgram(self):
        exit()

    def openFile(self):
        name= fd.askopenfilename() 
        print(name)

    def openDir(self):
        dirName = fd.askdirectory()
        print(dirName)

    def showMessage(self):
        alert.showinfo('Messaggio','testo del messaggio')
        print("showMessage")


        
root = Tk()
app = Window(root)
root.wm_title("ZipCycle")
root.geometry("620x400")
root.mainloop()


