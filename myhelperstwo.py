from codonchartimport import *

def checkifgenesalign(mrna,utr):
    #This is to check if both of the files have the exactly the same number and gene types
    #When matching, dictionaries do not care about the order
    check = mrna.keys() == utr.keys()
    if check == True:
        print("they match")
        return True

    else:
        print("they don't match")
        return False

def removeutrregions(mrnadict, utrdict):
    #This will take both dictionaries and use the information from the utr region from the utr dictionary to remove the utr region from the transcript
    #for key, value in utr.items():
    #    print(key, value) 

    for gene, utr in utrdict.items():

        mrnadict[gene] = mrnadict[gene][utr:]

    return mrnadict

def firstxnucleotides(transcript):
    nucleotidenumber = 60
    return transcript[:nucleotidenumber]

def aminoacidtranslation(transcript):

    mycodonchart = codonchart()
    tripletsequence = transcript[:3]
    
    if len(tripletsequence) == 0:
        return 0

    elif len(tripletsequence) == 3:
        return mycodonchart[tripletsequence] + aminoacidtranslation(transcript[3:])
        
    
"""
def main():

    maturernadict = removeutrregions(dict1, dict2)
    for key, value in maturernadict.items():
        print(aminoacidtranslation(value))

main()"""