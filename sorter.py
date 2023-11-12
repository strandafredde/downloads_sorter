import os
import shutil



#Function to check if the specifed folder exist
def does_folder_exist(folder_name):
    download_directory = os.path.join(os.path.expanduser("~"), "Downloads") # This assumes the Downloads folder is in the user's home directory
    folder_path = os.path.join(download_directory, folder_name)

    return os.path.exists(folder_path) and os.path.isdir(folder_path)


def make_folder(folder_name):
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    folder_path = os.path.join(downloads_path, folder_name)
    os.mkdir(folder_path)



def sort_download_dir():
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        entries = os.listdir(downloads_path)

    except:
        print("Could not access directory")

    else:

        #Checks if folders that are used to store files exist, if not creates them
        if not does_folder_exist("ZIP"):
            print("ZIP folder does not exist, creating one ")
            make_folder("ZIP")

        if not does_folder_exist("PDF"):
            print("PDF folder does not exist, creating one")
            make_folder("PDF")

        if not does_folder_exist("FOLDERS"):
            print("FOLDERS folder does not exist, creating one")
            make_folder("FOLDERS")

        if not does_folder_exist("PICTURES"):
            print("PICTURES folder does not exist, creating one")
            make_folder("PICTURES")

        if not does_folder_exist("MISCELLANEOUS"):
            print("MISCELLANEOUS folder does not exist, creating one")
            make_folder("MISCELLANEOUS")


        #Goes trough all the files in "Downloads" and stores them in their corresponding folder 
        for files in entries:
            file_path = os.path.join(downloads_path, files)

            #PDF files
            if ".pdf" in files:
                file_path = os.path.join(downloads_path, files)
                folder_path = os.path.join(downloads_path, "PDF")
                shutil.move(file_path, folder_path)

            #IMAGES
            if ".png" in files or ".jpg" in files or ".jpeg" in files or ".webp" in files:
                file_path = os.path.join(downloads_path, files)
                folder_path = os.path.join(downloads_path, "PICTURES")
                shutil.move(file_path, folder_path)

            #ZIP files
            if ".zip" in files or ".rar" in files:
                file_path = os.path.join(downloads_path, files)
                folder_path = os.path.join(downloads_path, "ZIP")
                shutil.move(file_path, folder_path)             

            #FOLDERS
            if os.path.isdir(downloads_path):
                if files != "ZIP" and files != "PDF" and files != "PICTURES" and files != "FOLDERS" and files != "MISCELLANEOUS":
                    file_path = os.path.join(downloads_path, files)
                    if os.path.isdir(file_path):
                        file_path = os.path.join(downloads_path, files)
                        folder_path = os.path.join(downloads_path, "FOLDERS")
                        shutil.move(file_path, folder_path)

            #MISCELLANEOUS files
            elif files != "ZIP" and files != "PDF" and files != "PICTURES" and files != "FOLDERS" and files != "MISCELLANEOUS":
                file_path = os.path.join(downloads_path, files)
                folder_path = os.path.join(downloads_path, "MISCELLANEOUS")
                shutil.move(file_path, folder_path)   

        print("Files sorted")

sort_download_dir()