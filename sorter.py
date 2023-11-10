import os
import shutil

try:
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    entries = os.listdir(downloads_path)
except:
    print("Could not access directory")
else:
    for files in entries:
        #PDF files
        if ".pdf" in files:
            file_path = os.path.join(downloads_path, files)
            folder_path = os.path.join(downloads_path, "PDF")
            shutil.move(file_path, folder_path)
            #print (file_path)

        #IMAGES
        if ".png" in files or ".jpg" in files or ".jpeg" in files or "webp" in files:
            file_path = os.path.join(downloads_path, files)
            folder_path = os.path.join(downloads_path, "PICTURES")
            shutil.move(file_path, folder_path)
            #print (file_path)

        #ZIP files
        if ".zip" in files or "rar" in files:
            file_path = os.path.join(downloads_path, files)
            folder_path = os.path.join(downloads_path, "ZIP")
            shutil.move(file_path, folder_path)
            #print (file_path)
        if os.path.isdir(downloads_path) and "ZIP" not in downloads_path and "PICTURES" not in downloads_path and "PDF" not in downloads_path:
            print(files)