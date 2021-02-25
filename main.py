
import os
from os.path import join
from glob import glob
import zipfile

CF = input("Inserisci CF: ") 
print(CF) 
AP = input("Inserisci (A) per Fatture Attive (P) per passive: ") 
print(AP) 

# rimuovi i files di metadati
base_dir = 'C://xdata/'
for filepath in glob(base_dir + '*_metaDato.xml'):
    print(filepath)
    os.remove(filepath)
    

# Rileva la lista dei files nella directory
files = []
files.extend(glob(join(base_dir, '*.*')))

print(files)



# crea dei files zip di contenente al massimo 10 files xml
counter = 1
nfiles = len(files)
counter_gruppo = 1
gruppo = []

for file in files:
    print(counter, end=': ')
    #print(file)
    gruppo.append(file)

    if counter %10 == 0 or counter == nfiles:
        nome_file_zip = 'IT'+CF+'_19'+AP+str(counter_gruppo).zfill(2)+'.zip'
        ziph = zipfile.ZipFile(base_dir+nome_file_zip, 'w', zipfile.ZIP_DEFLATED)

        print(gruppo)
        for file_nel_gruppo in gruppo:
            print('file_nel_gruppo', end=': ')
            print(os.path.basename(file_nel_gruppo))
            ziph.write(file_nel_gruppo,os.path.basename(file_nel_gruppo))
        ziph.close()
        print ('gruppo 2019:'+str(counter_gruppo)+' fine gruppo fai zip : '+nome_file_zip)
        gruppo = []
        counter_gruppo += 1

    counter += 1


