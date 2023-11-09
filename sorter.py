import os

try:
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    entries = os.listdir(downloads_path)
except:
    print("Could not access directory")
else:
    for files in entries:
        if ".pdf" in files:
            print (files)