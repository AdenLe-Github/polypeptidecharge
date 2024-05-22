from myhelpers import *
from myhelperstwo import *
import os

def controlpanel():
    print("\n\n\n")
    mrnadictionary = formattingmrna("inputcode/mrnatranscripts/mrna.txt")
    utrdictionary = formatting_utr("inputcode/utrregions/utrregions.txt")

    checkifgenesalign(mrnadictionary, utrdictionary)
    if checkifgenesalign:
        maturedmrnadictionary = removeutrregions(mrnadictionary, utrdictionary)
        polypetide = aminoacidtranslation(maturedmrnadictionary)

    



controlpanel()