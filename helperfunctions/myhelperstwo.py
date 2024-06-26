from helperfunctions.codonchartimport import *

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

def firstxaminoacidinput():
    #This returns the given transcript with the first "x" amount of nucleotides
    aminoacid = int(input("Amino acids do you want to analyze?"))
    return aminoacid


def firstxnucleotides(transcript, aminoacidcount):
    #This returns the given transcript with the first "x" amount of nucleotides
    nucleotidenumber = aminoacidcount * 3
    return transcript[:nucleotidenumber]

def aminoacidtranslationforcharge(transcript):
    #Uses the imported codon chart to give the overall charge for the given transcript
    mycodonchart = codonchartcharge()
    tripletsequence = transcript[:3]
    
    if len(tripletsequence) == 0:
        return 0

    elif len(tripletsequence) == 3:
        return mycodonchart[tripletsequence] + aminoacidtranslationforcharge(transcript[3:])


def aminoacidtranslationforpolypeptide(transcript):
    #Returns a list with all of the translated amino acids from the given transcript
    mycodonchart = codonchartregular()
    tripletsequence = transcript[:3]
    if len(tripletsequence) == 0:
        return []
    
    elif len(tripletsequence) == 3:
        polypeptidechain = [mycodonchart[tripletsequence]]
        polypeptidechain.extend(aminoacidtranslationforpolypeptide(transcript[3:]))
        return polypeptidechain
    
def aminoacidtranslationforsize(transcript):
    #Uses the imported codon chart to give the overall charge for the given transcript
    mycodonchart = codonchartsize()
    tripletsequence = transcript[:3]
    
    if len(tripletsequence) == 0:
        return 0

    elif len(tripletsequence) == 3:
        return mycodonchart[tripletsequence] + aminoacidtranslationforsize(transcript[3:])

def aminoacidtranslationforhydropathy(transcript):
    #Uses the imported codon chart to give the overall charge for the given transcript
    mycodonchart = codoncharthydro()
    tripletsequence = transcript[:3]
    
    if len(tripletsequence) == 0:
        return 0

    elif len(tripletsequence) == 3:
        return mycodonchart[tripletsequence] + aminoacidtranslationforhydropathy(transcript[3:])
    
def aminoacidtranslationformass(transcript):
    #Uses the imported codon chart to give the overall charge for the given transcript
    mycodonchart = codonchartmass()
    tripletsequence = transcript[:3]
    
    if len(tripletsequence) == 0:
        return 0

    elif len(tripletsequence) == 3:
        return mycodonchart[tripletsequence] + aminoacidtranslationformass(transcript[3:])


    



    
        
    
