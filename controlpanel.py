from helperfunctions.myhelpers import *
from helperfunctions.myhelperstwo import *
from helperfunctions.codonchartimport import *
import os

"""This code processes the data for the output that we are interested in, the overall charge of the polypetide chain
for the first "x" amount of nucleotides, disregarding the UTR region"""

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
            #Translates the sequence and gives the overall charge for the "x" amount of amino acids
            maturedmrnadictionary[key] = aminoacidtranslationforcharge(maturedmrnadictionary[key])

        with open("outputcode/output.txt", "w") as outputfile:
            outputfile.write("Gene name, Transcript overall charge")
            for key, value in maturedmrnadictionary.items():
                outputfile.write("\n")
                outputfile.write(f"{key}, {value}")
        

    else:
        #If the genes don't align 
        print("The genes do not align: ERROR")
        exit()




controlpanel()