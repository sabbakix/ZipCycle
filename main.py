
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
for file in files:
    print(counter, end=': ')
    print(file)
    counter += 1