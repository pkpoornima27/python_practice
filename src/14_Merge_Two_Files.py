import os

folder_path = input("Enter the path")

if not os.path.isdir(folder_path):
    print("invalid directory path")
else:
    output_file = os.path.join(folder_path, "merged.txt")

    with open(output_file, "w") as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt") and filename!= "merged.txt":
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
                print(f"Merged: {filename}")