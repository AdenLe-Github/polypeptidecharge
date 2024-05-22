import os

def isthereafile():
    # Accept from the user the name of a file containing the data.
    # If no file of that name exists, print an error message and quit.

    # Accept the file name from the user
    filename = input("Enter data filename: ").strip()

    # Check that the file exists. (Does not exist)
    if not os.path.isfile(filename):
        print("Cannot find file: " + filename)
        return None

    #File Exists
    if os.path.isfile(filename):
        print("Creating product database from file: " + filename)
        print()
        return filename
    
"""def sortsinfointodictionary(filename):
    with open(filename, "r") as insidefile:
        for line in insidefile:
            print(line)
"""

def controlpanel():
    isthereafile()

controlpanel()

    
