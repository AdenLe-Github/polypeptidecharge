from helperfunctions.myhelpers import *
from helperfunctions.myhelperstwo import *
from helperfunctions.codonchartimport import *
import os
def spacer():
    #Function for visual clarity
    print("\n\n")

def controlpanel():
    #Retrieves the mRNA file and formats the information into a dictionary where it is {gene: nt sequence}
    mrnadictionary = formattingmrna(retrieve_mrna())

    #Retrieves the UTR file and formats the information into a dictionary where it is {gene: UTR size}
    utrdictionary = formatting_utr(retrieve_utr())

    #Before the program fully starts, this function checks if the same genes are there for each of the dictionaries
    checkifgenesalign(mrnadictionary, utrdictionary)
    if checkifgenesalign:
        #Splices out the utr region
        maturedmrnadictionary = removeutrregions(mrnadictionary, utrdictionary)
        spacer()
        for key, value in maturedmrnadictionary.items():
            #isolates the first "x" nucleotides
            maturedmrnadictionary[key] = firstxnucleotides(value)
            #Translates the sequence and returns a list that is given to each gene which has the first "x" amount of amino acids
            maturedmrnadictionary[key] = aminoacidtranslationforpolypeptide(maturedmrnadictionary[key])

        #Writes the new data in another file
        with open("outputdata/outputvalidate.txt", "w") as outputfile:
                emptyset = set()
                validationset = set("M")
                for key, value in maturedmrnadictionary.items():
                    #For the code to be validated, we only want "M" in the set
                    emptyset.add(value[0])
                    outputfile.write("\n")
                    outputfile.write(f"{key}, {value}")

                if emptyset == validationset:
                    print(emptyset)
                    print("The code is validated")

                else:
                     print(emptyset)
                     print("The code can't be validated, there is an error")


    else:
        #If the genes don't align 
        print("The genes do not align: ERROR")
        exit()





controlpanel()