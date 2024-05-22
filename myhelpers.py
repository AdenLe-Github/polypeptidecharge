import os
import re

def check_file_in_folder(folder, filename):
    #Checks within folders
    full_path = os.path.join(folder, filename)
    #returns the full_path of the file
    print(full_path)
    return os.path.isfile(full_path), full_path

def retrieve_mrna():
    #Used to retrieve the mRNA file if it exists and the folder_path is correct
    print("\n\n\n")

    #If the inputcode or the mrnatranscript file have been altered, the folder_path must be changed
    folder_path = "inputcode/mrnatranscripts"
    file_name = input("Input the filename containing the mRNA transcript, make sure to include the \nfile type in the end, (ex: filename.txt): ")
    
    file_exists = check_file_in_folder(folder_path, file_name)
    print(f"File '{file_name}' exists: {file_exists[0]}")

    return file_exists[1]

def formattingmrna(filename):
    #Seperates the gene from it's transcript and inserts them both in a dictionary 
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
    insidefile.close()

    with open(filename, "r") as insidefile:
        for line in insidefile:

            if ">" in line:
                count += 1
                emptydict[line[1:].strip()] = finalizedlist[count]

    insidefile.close()
    return emptydict

def retrieve_utr():
    #Retrieves the 5' UTR file from the correct folder
    print("\n\n\n")

    #If the inputcode or the mrnatranscript file have been altered, the folder_path must be changed
    folder_path = "inputcode/utrregions"
    file_name = input("Input the filename containing the utrregion information, make sure to include the \nfile type in the end, (ex: filename.txt): ")
    
    file_exists = check_file_in_folder(folder_path, file_name)
    print(f"File '{file_name}' exists: {file_exists[0]}")

    return file_exists[1]


def formatting_utr(filename):
    #Gets rid of all extraneous information from the file and puts them in a dictionary with the gene name and the size of the 5' UTR region
    emptydict = {}
    emptylist = []
    count = -1
    conjoinedline  = ""
    with open(filename, "r") as insidefile:
        for line in insidefile:

            if "UTR5" in line:

                for i in range (2):
                    #finds the first white space character from the left
                    match = re.search(r"\s", line)
                    # Retrieves the index of the first white space character
                    index = match.start()
                    line = line[index:].strip()

                secondmatch = re.search(r"\s", line)
                index = secondmatch.start()
                line = line[:index].strip()
                emptylist.append(int(line))

            else:
                continue

        insidefile.close()

    with open(filename, "r") as insidefile:
        for line in insidefile:

            if "UTR5" in line:
                count += 1
                #finds the first white space character from the left
                match = re.search(r"\s", line)
                # Retrieves the index of the first white space character
                index = match.start()
                line = line[:index].strip()
                
                emptydict[line] = emptylist[count]

    return emptydict


    
