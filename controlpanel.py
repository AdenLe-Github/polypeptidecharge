from helperfunctions.myhelpers import *
from helperfunctions.myhelperstwo import *
from helperfunctions.codonchartimport import *
import os
import copy  # Importing the copy module for deep copy

"""This code processes the data for the output that we are interested in, the overall charge of the polypetide chain
for the first "x" amount of nucleotides, disregarding the UTR region"""

def spacer():
    #Function for visual clarity
    print("\n")

def switchcheck():
    check = input("Would you like to quit or go again? (Y)/(N): ")
    if check.lower() == "y":
        return True
    elif check.lower() == "n":
        print("The code will now terminate. Thank you!")
        return False
    else:
        print("Invalid input.")
        return switchcheck()



def controlpanel():
    switch = True
    #Retrieves the mRNA file and formats the information into a dictionary where it is {gene: nt sequence}
    mrnadictionary = formattingmrna(retrieve_mrna())

    #Retrieves the UTR file and formats the information into a dictionary where it is {gene: UTR size}
    utrdictionary = formatting_utr(retrieve_utr())
    
    #Before the program fully starts, this function checks if the same genes are there for each of the dictionaries
    checkifgenesalign(mrnadictionary, utrdictionary)

    if checkifgenesalign:
        print("Both datasets contain the same genes")

        #Splices out the utr region
        basematuredmrnadictionary = removeutrregions(mrnadictionary, utrdictionary)
        
        spacer()
        print("The UTR region has been spliced out")
        spacer()

        while switch == True:
            maturedmrnadictionary = copy.deepcopy(basematuredmrnadictionary)
            #Takes how many amino acids you would want to be analyzed
            aminoacidcount = firstxaminoacidinput()
            spacer()
            #Asks for the function you would like to perform
            branchone = input("What function would you like to perform?\n\n - Sequence the \"x\" nucleotides (A): \n - Calculate the overall charge of the sequence for \"x\" nucleotides (B): \n - Calculate the molecular weight for \"x\" nucleotides (C):")
            
            if branchone.lower() == "a":
                #Sequences the transcript for the first "x" amino acids
                for key, value in maturedmrnadictionary.items():
                    #isolates the first "x" nucleotides
                    maturedmrnadictionary[key] = firstxnucleotides(value, aminoacidcount)
                    #Translates the sequence and returns a list that is given to each gene which has the first "x" amount of amino acids
                    maturedmrnadictionary[key] = aminoacidtranslationforpolypeptide(maturedmrnadictionary[key])

                #Writes the new data in another file
                output_file_name = input("Enter the output file name (without extension): ")
                with open(f"outputdata/{output_file_name}.txt", "w") as outputfile:
                    emptyset = set()
                    validationset = set("M")
                    for key, value in maturedmrnadictionary.items():
                        emptyset.add(value[0])
                        outputfile.write(f"{key}, {value}")
                        outputfile.write("\n")

                    #For the code to be validated, we only want "M" in the set
                    if emptyset == validationset:
                        print(emptyset)
                        print("The code is validated")

                    else:
                        print(emptyset)
                        print("The code can't be validated, there is an error")
                
                switch = switchcheck()

            elif branchone.lower() == "b":
                for key, value in maturedmrnadictionary.items():
                    #isolates the first "x" nucleotides
                    maturedmrnadictionary[key] = firstxnucleotides(value, aminoacidcount)
                    #Translates the sequence and gives the overall charge for the "x" amount of amino acids
                    maturedmrnadictionary[key] = aminoacidtranslationforcharge(maturedmrnadictionary[key])
                
                #Writes the new data in another file
                output_file_name = input("Enter the output file name (without extension): ")
                with open(f"outputdata/{output_file_name}.txt", "w") as outputfile:
                    outputfile.write("Gene name, Transcript overall charge")
                    for key, value in maturedmrnadictionary.items():
                        outputfile.write("\n")
                        outputfile.write(f"{key}, {value}")

                switch = switchcheck()

            elif branchone.lower() == "c":
                for key, value in maturedmrnadictionary.items():
                    #isolates the first "x" nucleotides
                    maturedmrnadictionary[key] = firstxnucleotides(value, aminoacidcount)
                    #Translates the sequence and gives the overall charge for the "x" amount of amino acids
                    maturedmrnadictionary[key] = aminoacidtranslationforsize(maturedmrnadictionary[key])
                #Writes the new data in another file
                output_file_name = input("Enter the output file name (without extension): ")
                with open(f"outputdata/{output_file_name}.txt", "w") as outputfile:
                    outputfile.write("Gene name, Transcript overall size")
                    for key, value in maturedmrnadictionary.items():
                        outputfile.write("\n")
                        outputfile.write(f"{key}, {value}")

                switch = switchcheck()

            else:
                #If the genes don't align 
                print("The genes do not align: ERROR")
                switch = switchcheck()




controlpanel()