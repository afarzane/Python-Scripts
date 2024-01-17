# This simple program is developed to find folders with the largest size in every drive
# I created it to make my life easier when it came to cleaning my drives.
# Code works best on drives with less data as takes a while if you want to check all drives, 
# so if you're impatient and require results right away, change "drive_path" into the specific
# drive you want to check and comment out the loop.
# --------------------------------------------------------------------------------------------
# Author: Amirali Farzaneh
# Date: January 16th, 2024

import os
from concurrent.futures import ThreadPoolExecutor

def get_folder_size(folder_path):
    total_size = 0
    with ThreadPoolExecutor() as executor:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            file_sizes = list(executor.map(lambda name: os.path.getsize(os.path.join(dirpath, name)), filenames))
            total_size += sum(file_sizes)
    return total_size

def find_largest_folder(path, i):
    if os.path.exists(path):
        largest_folder = ""
        largest_size = 0
        indents = " " * i
        print(f"{indents}Largest file in directory {path}:")
        dirs = os.listdir(path)
        for dir in dirs:
            folder_path = os.path.join(path, dir)
            current_size = get_folder_size(folder_path)
            if current_size > largest_size:
                largest_size = current_size
                largest_folder = folder_path
                
        print(f"{indents}Folder: {largest_folder}")
        print(f"{indents}Size: {largest_size / (1024 ** 3):.2f} GB")

        entries = os.listdir(largest_folder)
        folders = [entry for entry in entries if os.path.isdir(os.path.join(largest_folder, entry))]
        if folders:
            find_largest_folder(largest_folder, i+5)

    else:
        exit()


def main():
    # drives = [d for d in os.popen("wmic logicaldisk get caption").read().split()[1:]]

    # for drive in drives:
    i = 0
    drive_path = f"C:\\"
    find_largest_folder(drive_path, i)

    # ---------- Testing play ground ---------- #
    # entries = os.listdir(drive_path)
    # if entries:
    #     print("Entries exist")
    # else:
    #     print("Directory empty")
    #     return
    

if __name__ == "__main__":
    main()