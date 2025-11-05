#13. File Renamer Script
import os
folder_path = "/home/purniema/Documents/python"
prefix = "new_"

for filename in os.listdir(folder_path):
    print("filename:", filename)
    if filename.endswith(".txt"):
        old_path = os.path.join(folder_path, filename)
        new_name = prefix + filename
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

