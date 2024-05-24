# polypeptidecharge
This program will sequence a mRNA transcript in regards to the 5' UTR region and will then calculate the overall charge of the polypeptide chain up to "x" amino acid.

In the Folder HelperFunctions Stores all of the functions necessary for processing the inputted data. Within the file myhelperstwo.py, for the function firstxnucleotides, the nucleotidenumber can be changed to alter the number of nucleotides being translated, post 5' UTR removal.

The control panel is where the main code will be ran and the results will be seen in output.txt

The datavalidation.py is to check if the code has ran correctly and their are logic errors. The set that is printed should just contain {"M"} as that is the defined starting amino acid.

In the codonchartimport.py in the helperfucntions folder, you can alter the charge given by each of the amino acid based on the environment the amino acid is in (pH)

Finally, it is essentially to later the pathway in the myhelpers.py in the file retriever functions if the file pathway is changed in the code