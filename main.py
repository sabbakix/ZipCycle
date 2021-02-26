
import os
from os.path import join
from glob import glob
import zipfile

CF = input("Inserisci CF: ") 
print(CF) 
AP = input("Inserisci (A) per Fatture Attive (P) per passive: ")
print(AP) 

if AP == '' or CF == '':
    exit()


#Directory di base
base_dir = 'C://xdata/'
tmp_dir = 'C://tmp/'


# Ripulisci la dir temporanea
for filepath in glob(tmp_dir + '*.*'):
    print('Ripulisci la dir temporanea: ', end='')
    print(filepath)
    os.remove(filepath)


# Controllo che la dir temporanea sia vuota
for filepath in glob(tmp_dir + '*.*'):
    print('Controllo che la dir temporanea sia vuota: ', end='')
    print(filepath)
    if len(filepath) != 0:
        exit()


# Rileva la lista dei files nella directory dati
files_zip = []
files_zip.extend(glob(join(base_dir, '*.*')))


# Estrai i files Zip nella dir temporanea
for file_zip in files_zip:
    print('Estrai i files Zip: ', end='')
    print(file_zip)
    with zipfile.ZipFile(file_zip,"r") as zip_ref:
        zip_ref.extractall(tmp_dir)


# Rimuovi i files di metadati
for filepath in glob(tmp_dir + '*_metaDato.xml'):
    print('Rimuovi i files di metadati: ', end='')
    print(filepath)
    os.remove(filepath)


# Rileva la lista dei files rimasti nella directory temporanea
files = []
files.extend(glob(join(tmp_dir, '*.*')))
print('Rileva la lista dei files rimasti nella directory temporanea: ')
print(files)


# crea dei files zip contenenti al massimo 10 files
counter = 1
nfiles = len(files)
counter_gruppo = 1
gruppo = []

for file in files:
    print(counter, end=': ')
    print(file)
    gruppo.append(file)

    if counter %10 == 0 or counter == nfiles:
        nome_file_zip = 'IT'+CF+'_19'+AP+str(counter_gruppo).zfill(2)+'.zip'
        ziph = zipfile.ZipFile(base_dir+nome_file_zip, 'w', zipfile.ZIP_DEFLATED)

        #print(gruppo)
        for file_nel_gruppo in gruppo:
            print('file_nel_gruppo', end=': ')
            print(os.path.basename(file_nel_gruppo))
            ziph.write(file_nel_gruppo,os.path.basename(file_nel_gruppo))
        ziph.close()
        print ('gruppo: '+str(counter_gruppo)+' zip : '+nome_file_zip)
        gruppo = []
        counter_gruppo += 1

    counter += 1
