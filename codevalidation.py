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
            maturedmrnadictionary[key] = aminoacidtranslationforpolypeptide(maturedmrnadictionary[key])

        with open("outputcode/outputvalidate.txt", "w") as outputfile:
                emptyset = set()
                for key, value in maturedmrnadictionary.items():
                    emptyset.add(value[0])
                    outputfile.write("\n")
                    outputfile.write(f"{key}, {value}")

                print(emptyset)


    else:
        print("The genes do not align: ERROR")
        exit()





controlpanel()