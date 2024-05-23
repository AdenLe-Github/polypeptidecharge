from myhelpers import *
from myhelperstwo import *
from codonchartimport import *
import os
def spacer():
    print("\n\n")

def controlpanel():
    mrnadictionary = formattingmrna(retrieve_mrna())
    utrdictionary = formatting_utr(retrieve_utr())

    checkifgenesalign(mrnadictionary, utrdictionary)
    if checkifgenesalign:
        maturedmrnadictionary = removeutrregions(mrnadictionary, utrdictionary)
        spacer()
        for key, value in maturedmrnadictionary.items():
            maturedmrnadictionary[key] = firstxnucleotides(value)
            maturedmrnadictionary[key] = aminoacidtranslationforcharge(maturedmrnadictionary[key])

        with open("outputcode/output.txt", "w") as outputfile:
            outputfile.write("Gene name, Transcript overall charge")
            for key, value in maturedmrnadictionary.items():
                outputfile.write("\n")
                outputfile.write(f"{key}, {value}")
        

    else:
        print("The genes do not align: ERROR")
        exit()




controlpanel()