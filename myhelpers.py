import os

def check_file_in_folder(folder, filename):
    #Checks within folders
    full_path = os.path.join(folder, filename)
    #returns the full_path of the file
    print(full_path)
    return os.path.isfile(full_path), full_path

def retrieve_mrna():
    print("\n\n\n")

    #If the inputcode or the mrnatranscript file have been altered, the folder_path must be changed
    folder_path = "inputcode/mrnatranscripts"
    file_name = input("Input the filename containing the mRNA transcript, make sure to include the \nfile type in the end, (ex: filename.txt): ")
    
    file_exists = check_file_in_folder(folder_path, file_name)
    print(f"File '{file_name}' exists: {file_exists[0]}")

    return file_exists[1]

def formattingmrna(filename):
    print("\n\n\n")
    emptydict = {}
    emptylist = []
    count = -1
    conjoinedline  = ""
    with open(filename, "r") as insidefile:
        for line in insidefile:

            if ">" not in line:
                conjoinedline += str(line.strip())

            if ">" in line:
                emptylist.append(conjoinedline)
                conjoinedline = ""

        emptylist.append(conjoinedline)
        finalizedlist = emptylist[1:]

    with open(filename, "r") as insidefile:
        for line in insidefile:

            if ">" in line:
                count += 1
                emptydict[line[1:].strip()] = finalizedlist[count]
                

    return emptydict
