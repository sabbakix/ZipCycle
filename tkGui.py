import sys
import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog
import tkinter.messagebox



class App:

    def __init__(self, root):

        #setting title
        root.title("Zip ADE")
        #setting window size
        width=800
        height=600
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
        #self.fileMenu.add_command(label="Mostra messaggio", command=self.showMessage)
        self.fileMenu.add_command(label="Esci", command=self.eseguiEsciButton)
        self.menu.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu = tk.Menu(self.menu)
        self.editMenu.add_command(label="Undo")
        self.editMenu.add_command(label="Redo")
        self.menu.add_cascade(label="Help", command=self.showMessage)

        

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
        self.entry01["borderwidth"] = 2
        self.entry01["relief"] = "groove"
        self.entry01.place(x=140,y=10,width=630,height=30)
        self.entry01.configure(state=tk.DISABLED)
        self.entry01.config(fg = 'blue')

        

        self.listbox01=tk.Listbox(root)
        self.listbox01["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listbox01["font"] = ft
        self.listbox01["fg"] = "#333333"
        self.listbox01["justify"] = "left"
        self.listbox01.place(x=10,y=250,width=760,height=301)
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
        self.avviaButton.place(x=660,y=560,width=111,height=30)
        self.avviaButton["command"] = self.eseguiAvviaButton


        self.clearButton=tk.Button(root)
        self.clearButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.clearButton["font"] = ft
        self.clearButton["fg"] = "#000000"
        self.clearButton["justify"] = "center"
        self.clearButton["text"] = "Pulisci"
        self.clearButton.place(x=530,y=560,width=121,height=30)
        self.clearButton["command"] = self.eseguiClearButton

        self.esciButton=tk.Button(root)
        self.esciButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.esciButton["font"] = ft
        self.esciButton["fg"] = "#000000"
        self.esciButton["justify"] = "center"
        self.esciButton["text"] = "Esci"
        self.esciButton.place(x=400,y=560,width=121,height=30)
        self.esciButton["command"] = self.eseguiEsciButton

        


        self.cflabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.cflabel["font"] = ft
        self.cflabel["fg"] = "#333333"
        self.cflabel["justify"] = "right"
        self.cflabel["text"] = "Codice Fiscale: "
        self.cflabel["relief"] = "groove"
        self.cflabel.place(x=10,y=50,width=130,height=25)

        self.cfentry02=tk.Entry(root)
        self.cfentry02["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.cfentry02["font"] = ft
        self.cfentry02["fg"] = "#333333"
        self.cfentry02["justify"] = "left"
        self.cfentry02["text"] = "CF"
        self.cfentry02.place(x=140,y=50,width=340,height=25)

        self.checkbutton01=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        self.checkbutton01["font"] = ft
        self.checkbutton01["fg"] = "#333333"
        self.checkbutton01["justify"] = "center"
        self.checkbutton01["text"] = "  File di origine è  zip"
        self.checkbutton01.place(x=330,y=50,width=198,height=30)
        self.checkbutton01["offvalue"] = "0"
        self.checkbutton01["onvalue"] = "1"
        self.checkbutton01["command"] = self.checkbutton01_command

        self.apradiobutton01=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        self.apradiobutton01["font"] = ft
        self.apradiobutton01["fg"] = "#333333"
        self.apradiobutton01["justify"] = "center"
        self.apradiobutton01["text"] = "Attive"
        self.apradiobutton01.place(x=520,y=55,width=85,height=25)
        self.apradiobutton01["value"] = "Attive"
        self.apradiobutton01["command"] = self.apradiobutton01_command

        self.apradiobutton02=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        self.apradiobutton02["font"] = ft
        self.apradiobutton02["fg"] = "#333333"
        self.apradiobutton02["justify"] = "center"
        self.apradiobutton02["text"] = "Passive"
        self.apradiobutton02["relief"] = "flat"
        self.apradiobutton02.place(x=600,y=55,width=85,height=25)
        self.apradiobutton02["value"] = "Passive"
        self.apradiobutton02["command"] = self.apradiobutton02_command

        self.textbox01=tk.Text(root)
        ft = tkFont.Font(family='Times',size=10)
        self.textbox01["font"] = ft
        self.textbox01["fg"] = "#333333"
        #["justify"] = "left"
        self.textbox01["relief"] = "groove"
        self.textbox01.place(x=11,y=120,width=760,height=122)
        self.textbox01.insert(tk.INSERT, "testo dtestoesto dtesto dtesto dtesto esto dtesto dtesto ")
        self.textbox01.configure(state=tk.DISABLED)

    def apradiobutton01_command(self):
        print("command")


    def apradiobutton02_command(self):
        print("command")


    def checkbutton01_command(self):
        print("command")

        

    def selDir01(self):
        dirName= tk.filedialog.askdirectory()
        self.entry01.configure(state=tk.NORMAL)
        self.entry01.delete(0,tk.END)
        self.entry01.insert(0,dirName)
        print("dir: ",dirName)
        self.entry01.configure(state=tk.DISABLED)

    def showMessage(self):
        tk.messagebox.showinfo('Messaggio','Selezionare la cartella in cui ci sono le fatture. \
Le fatture devono essere in uno o piu zip. Cliccando il pulsant avvia \
verranno lette le fatture negli zip e rezippate in pacchetti da 10 fatture.')
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
        sys.exit()
    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
