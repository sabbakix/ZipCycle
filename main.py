
import os
from os.path import join
from glob import glob

# rimuovi i files di metadati
base_dir = 'C://xdata/'
for filepath in glob(base_dir + '*_metaDato.xml'):
    print(filepath)
    os.remove(filepath)
    

# Rileva la lista dei files nella directory
files = []
for ext in ('*.xml', '*.xml.p7m'):
    files.extend(glob(join(base_dir, ext)))

print(files)

# crea dei files zip di contenente al massimo 10 files xml
counter = 1
nfiles = len(files)
counter_gruppo = 1
for file in files:
    gruppo = []
    print(counter, end=': ')
    print(file)
    if counter %10 == 0 or counter == nfiles:
        print ('gruppo:'+str(counter_gruppo)+' fine gruppo fai zip')
        counter_gruppo += 1
    counter += 1