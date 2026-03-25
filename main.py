print('\nOrganizing files...\n')

import os

files = os.listdir()

FOLDERS = {
    'Images' : ['.jpg','.png','.jpeg'],
    'Documents' :['.md','.pdf','.txt'],
    'Video' : ['.mp4'],
    'Audio' : ['.mp3']
} 

for file in files:
    if file == 'main.py' or file == 'README.md':
        continue

    name , extension = os.path.splitext(file)
    extension = extension.lower()
    
    moved = False

    for folder,extensions in FOLDERS.items():
        if extension in extensions:
            if not os.path.exists(folder):
                os.makedirs(folder)
            os.rename(file,os.path.join(folder,file))
            print(f'{file}  ➡️  {folder}')
            moved = True 
            break

    if not moved:
        if not os.path.exists('Others'):
            os.makedirs("Others")
        os.rename(file, os.path.join("Others",file))
        print(f'{file}  ➡️  Others') 

print('\nDone Organizing ✅')