# polypeptidecharge
This program will sequence a mRNA transcript in regards to the 5' UTR region and will then calculate the overall charge of the polypeptide chain up to "x" amino acid.

                #finds the first white space character from the left
                match = re.search(r"\s", line)

                # Retrieves the index of the first white space character
                index = match.start()
                #Creates a new line where we get rid of the Gene name and the space in between
                newline = line[index:]
                #print(newline)
                secondformat = re.search("0", line)
                indextwo = secondformat.start()
                print(newline[indextwo: ].strip())


