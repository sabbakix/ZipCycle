import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog


class App:

    def __init__(self, root):

        #setting title
        root.title("Zip ADE")
        #setting window size
        width=800
        height=403
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.item_num = 0

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.fileMenu = tk.Menu(self.menu)
        self.fileMenu.add_command(label="Seleziona Cartella", command=self.selDir01)
        self.fileMenu.add_command(label="Mostra messaggio", command=self.showMessage)
        self.fileMenu.add_command(label="Esci", command=self.eseguiEsciButton)
        self.menu.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu = tk.Menu(self.menu)
        self.editMenu.add_command(label="Undo")
        self.editMenu.add_command(label="Redo")
        self.menu.add_cascade(label="Edit", menu=self.editMenu)

        

        self.selDirButton=tk.Button(root)
        self.selDirButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.selDirButton["font"] = ft
        self.selDirButton["fg"] = "#000000"
        self.selDirButton["justify"] = "center"
        self.selDirButton["text"] = "Seleziona Cartella"
        self.selDirButton.place(x=10,y=10,width=124,height=30)
        self.selDirButton["command"] = self.selDir01

        self.entry01=tk.Entry(root)
        self.entry01["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.entry01["font"] = ft
        self.entry01["fg"] = "#333333"
        self.entry01["justify"] = "left"
        self.entry01["text"] = "Entry"
        self.entry01["relief"] = "flat"
        self.entry01.place(x=140,y=10,width=630,height=30)

        

        self.listbox01=tk.Listbox(root)
        self.listbox01["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listbox01["font"] = ft
        self.listbox01["fg"] = "#333333"
        self.listbox01["justify"] = "left"
        self.listbox01.place(x=10,y=50,width=760,height=301)
        self.listbox01["yscrollcommand"] = True

        
        self.scrollbar = tk.Scrollbar(root) 
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH) 
        self.scrollbar.config(command = self.listbox01.yview) 
        self.listbox01.config(yscrollcommand = self.scrollbar.set)

        self.avviaButton=tk.Button(root)
        self.avviaButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.avviaButton["font"] = ft
        self.avviaButton["fg"] = "#000000"
        self.avviaButton["justify"] = "center"
        self.avviaButton["text"] = "Avvia"
        self.avviaButton.place(x=660,y=360,width=111,height=30)
        self.avviaButton["command"] = self.eseguiAvviaButton


        self.clearButton=tk.Button(root)
        self.clearButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.clearButton["font"] = ft
        self.clearButton["fg"] = "#000000"
        self.clearButton["justify"] = "center"
        self.clearButton["text"] = "Pulisci"
        self.clearButton.place(x=530,y=360,width=121,height=30)
        self.clearButton["command"] = self.eseguiClearButton

        self.esciButton=tk.Button(root)
        self.esciButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.esciButton["font"] = ft
        self.esciButton["fg"] = "#000000"
        self.esciButton["justify"] = "center"
        self.esciButton["text"] = "Esci"
        self.esciButton.place(x=400,y=360,width=121,height=30)
        self.esciButton["command"] = self.eseguiEsciButton

        


        

    def selDir01(self):
        dirName= tk.filedialog.askdirectory()
        self.entry01.delete(0,tk.END)
        self.entry01.insert(0,dirName)
        print("dir: ",dirName)

    def showMessage(self):
        tk.alert.showinfo('Messaggio','testo del messaggio')
        print("showMessage")


    def eseguiAvviaButton(self):

        for x in range(10):
            self.consolePrint(str(x)+"hello")

        print("Avvia Button")
    
    def consolePrint(self,text=""):
        output = str(self.item_num).zfill(3)+": "+text
        self.listbox01.insert(self.item_num, output)
        self.listbox01.see(self.item_num)
        self.item_num += 1
        

    def eseguiClearButton(self):
        print("Clearing ...")
        self.listbox01.delete(0,self.item_num)
        self.item_num = 0
    
    def eseguiEsciButton(self):
        print("Closing ...")
        exit()
    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
