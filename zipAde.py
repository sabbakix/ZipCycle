"""
zipAde Interfaccia principale.

"""


import sys
import os
from os.path import join
from glob import glob
import zipfile
import tempfile

#tkinter library
import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog
import tkinter.messagebox



class App:

    base_dir = "C:/xdata"
    temp_dir = 0

    CF = ""
    origineZip = False
    AP = ""



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
        self.entry01.insert(0,self.base_dir)
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
        self.listbox01.place(x=10,y=450,width=760,height=101)
        self.listbox01["yscrollcommand"] = True

        self.scrollbar = tk.Scrollbar(self.listbox01) 
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
        self.textbox01["relief"] = "groove"
        self.textbox01.place(x=11,y=120,width=760,height=322)
        self.textbox01.insert(tk.INSERT, "Seleziona la cartella con le fatture, compila il campo Codice Fiscale, e premi Avvia\n")
        self.textbox01.configure(state=tk.DISABLED)
        
        self.scrollbar02 = tk.Scrollbar(self.textbox01) 
        self.scrollbar02.pack(side = tk.RIGHT, fill = tk.Y)
        self.scrollbar02.config(command = self.textbox01.yview) 
        self.textbox01.config(yscrollcommand = self.scrollbar02.set)
        

    def apradiobutton01_command(self):
        self.AP = 'A'


    def apradiobutton02_command(self):
        self.AP = 'P'


    def checkbutton01_command(self):
        self.origineZip = True

        

    def selDir01(self):
        dirName= tk.filedialog.askdirectory()
        self.entry01.configure(state=tk.NORMAL)
        self.entry01.delete(0,tk.END)
        self.entry01.insert(0,dirName)
        print("dir: ",dirName)
        self.base_dir = dirName
        self.entry01.configure(state=tk.DISABLED)

    def showMessage(self):
        tk.messagebox.showinfo('Messaggio','Selezionare la cartella in cui ci sono le fatture. \
Le fatture devono essere in uno o piu zip. Cliccando il pulsant avvia \
verranno lette le fatture negli zip e rezippate in pacchetti da 10 fatture.')
        print("showMessage")


    def eseguiAvviaButton(self):

        """
        for x in range(100):
            self.consolePrint(str(x)+" Test listbox")
        print("Avvia Button")
        print(self.temp_dir.name)
        self.dprint("testo in \n textbox test \n test nuovo")
        """

        self.temp_dir = tempfile.TemporaryDirectory()
        print(self.temp_dir.name)

        # Controllo che la dir temporanea sia vuota
        for filepath in glob(self.temp_dir.name + '*.*'):
            print('Controllo che la dir temporanea sia vuota: ', end='')
            print(filepath)
            if len(filepath) != 0:
                self.dprint("Cartella temporanea non vuota")
                return self.temp_dir.cleanup()

        #Verifica cartella selezionata 
        if self.base_dir == "":
            self.dprint("Nessuna cartella selezionata.")
            return self.temp_dir.cleanup()
        
        # Verifica CF
        if len(self.cfentry02.get()) == 0:
            self.dprint("Nessun Codice Fiscale inserito.")
            return self.temp_dir.cleanup()


        # Rileva la lista dei files nella directory dati
        files_zip = []
        files_zip.extend(glob(join(self.base_dir, '*.zip')))
        if len(files_zip) == 0:
            self.dprint("Nessun File Zip trovato nella cartella selezionata.")
            return self.temp_dir.cleanup()

        # Estrai i files Zip nella dir temporanea
        for file_zip in files_zip:
            print('Estrai i files Zip: ', end='')
            print(file_zip)
            with zipfile.ZipFile(file_zip,"r") as zip_ref:
                zip_ref.extractall(self.temp_dir.name)

        # Rimuovi i files di metadati
        for filepath in glob(self.temp_dir.name + '\*_metaDato.xml'):
            self.dprint('Ignora file di metadati: ', end='')
            self.dprint(filepath)
            os.remove(filepath)

        self.dprint ("")

        # Rileva la lista dei files rimasti nella directory temporanea
        files = []
        files.extend(glob(join(self.temp_dir.name, '*.*')))
        #self.dprint("")
        #self.dprint('Rileva la lista dei files rimasti nella directory temporanea: ')
        #self.dprint(files)

        # crea dei files zip contenenti al massimo 10 files
        counter = 1
        nfiles = len(files)
        counter_gruppo = 1
        gruppo = []
        self.CF = self.cfentry02.get()
        print(self.CF)
        print(self.AP)
        

        for file in files:
            self.dprint(counter, end=': ')
            self.dprint(file)
            gruppo.append(file)

            if counter %10 == 0 or counter == nfiles:
                nome_file_zip = 'IT'+self.CF+'_19'+self.AP+str(counter_gruppo).zfill(2)+'.zip'
                ziph = zipfile.ZipFile(self.base_dir+'/'+nome_file_zip, 'w', zipfile.ZIP_DEFLATED)

                #print(gruppo)
                for file_nel_gruppo in gruppo:
                    #self.dprint('file_nel_gruppo', end=': ')
                    #self.dprint(str(os.path.basename(file_nel_gruppo)))
                    ziph.write(file_nel_gruppo,os.path.basename(file_nel_gruppo))
                ziph.close()
                self.dprint ('inserite nel file: '+str(counter_gruppo)+' zip : '+nome_file_zip)
                self.dprint ("")
                gruppo = []
                counter_gruppo += 1

            counter += 1


        # Stampa files preseti in cartella temporanea
        for filepath in glob(self.temp_dir.name+'\*.*'):
            pass
            #self.dprint(filepath)
            #os.remove(filepath)

        self.temp_dir.cleanup()


        
        
    
    def consolePrint(self,text=""):
        output = str(self.item_num).zfill(3)+":  "+text
        self.listbox01.insert(self.item_num, output)
        self.listbox01.see(self.item_num)
        self.item_num += 1
        

    def eseguiClearButton(self):
        print("Clearing ...")
        self.listbox01.delete(0,self.item_num)
        self.item_num = 0
    
    def eseguiEsciButton(self):
        print("Closing ...")
        if self.temp_dir != 0:
            self.temp_dir.cleanup()
        sys.exit()
    
    def dprint(self,txt="", end="\n"):
        self.textbox01.configure(state=tk.NORMAL)
        self.textbox01.insert(tk.END, str(txt)+end)
        self.textbox01.see(tk.END)
        self.textbox01.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
