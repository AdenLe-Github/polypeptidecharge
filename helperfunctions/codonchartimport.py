def codonchartcharge():
    codontabcharge = {
        'TCA': 0,    # Serine
        'TCC': 0,    # Serine
        'TCG': 0,    # Serine
        'TCT': 0,    # Serine
        'TTC': 0,    # Phenylalanine
        'TTT': 0,    # Phenylalanine
        'TTA': 0,    # Leucine
        'TTG': 0,    # Leucine
        'TAC': 0,    # Tyrosine
        'TAT': 0,    # Tyrosine
        'TAA': 0,    # Stop
        'TAG': 0,    # Stop
        'TGC': 0,    # Cysteine
        'TGT': 0,    # Cysteine
        'TGA': 0,    # Stop
        'TGG': 0,    # Tryptophan
        'CTA': 0,    # Leucine
        'CTC': 0,    # Leucine
        'CTG': 0,    # Leucine
        'CTT': 0,    # Leucine
        'CCA': 0,    # Proline
        'CCC': 0,    # Proline
        'CCG': 0,    # Proline
        'CCT': 0,    # Proline
        'CAC': 1,    # Histidine
        'CAT': 1,    # Histidine
        'CAA': 0,    # Glutamine
        'CAG': 0,    # Glutamine
        'CGA': 1,    # Arginine
        'CGC': 1,    # Arginine
        'CGG': 1,    # Arginine
        'CGT': 1,    # Arginine
        'ATA': 0,    # Isoleucine
        'ATC': 0,    # Isoleucine
        'ATT': 0,    # Isoleucine
        'ATG': 0,    # Methionine
        'ACA': 0,    # Threonine
        'ACC': 0,    # Threonine
        'ACG': 0,    # Threonine
        'ACT': 0,    # Threonine
        'AAC': 0,    # Asparagine
        'AAT': 0,    # Asparagine
        'AAA': 1,    # Lysine
        'AAG': 1,    # Lysine
        'AGC': 0,    # Serine
        'AGT': 0,    # Serine
        'AGA': 1,    # Arginine
        'AGG': 1,    # Arginine
        'GTA': 0,    # Valine
        'GTC': 0,    # Valine
        'GTG': 0,    # Valine
        'GTT': 0,    # Valine
        'GCA': 0,    # Alanine
        'GCC': 0,    # Alanine
        'GCG': 0,    # Alanine
        'GCT': 0,    # Alanine
        'GAC': -1,   # Aspartic Acid
        'GAT': -1,   # Aspartic Acid
        'GAA': -1,   # Glutamic Acid
        'GAG': -1,   # Glutamic Acid
        'GGA': 0,    # Glycine
        'GGC': 0,    # Glycine
        'GGG': 0,    # Glycine
        'GGT': 0     # Glycine
    }
    return codontabcharge

def codonchartregular():
    codontab = {
    'TCA': 'S',    # Serine
    'TCC': 'S',    # Serine
    'TCG': 'S',    # Serine
    'TCT': 'S',    # Serine
    'TTC': 'F',    # Phenylalanine
    'TTT': 'F',    # Phenylalanine
    'TTA': 'L',    # Leucine
    'TTG': 'L',    # Leucine
    'TAC': 'Y',    # Tyrosine
    'TAT': 'Y',    # Tyrosine
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cysteine
    'TGT': 'C',    # Cysteine
    'TGA': '*',    # Stop
    'TGG': 'W',    # Tryptophan
    'CTA': 'L',    # Leucine
    'CTC': 'L',    # Leucine
    'CTG': 'L',    # Leucine
    'CTT': 'L',    # Leucine
    'CCA': 'P',    # Proline
    'CCC': 'P',    # Proline
    'CCG': 'P',    # Proline
    'CCT': 'P',    # Proline
    'CAC': 'H',    # Histidine
    'CAT': 'H',    # Histidine
    'CAA': 'Q',    # Glutamine
    'CAG': 'Q',    # Glutamine
    'CGA': 'R',    # Arginine
    'CGC': 'R',    # Arginine
    'CGG': 'R',    # Arginine
    'CGT': 'R',    # Arginine
    'ATA': 'I',    # Isoleucine
    'ATC': 'I',    # Isoleucine
    'ATT': 'I',    # Isoleucine
    'ATG': 'M',    # Methionine
    'ACA': 'T',    # Threonine
    'ACC': 'T',    # Threonine
    'ACG': 'T',    # Threonine
    'ACT': 'T',    # Threonine
    'AAC': 'N',    # Asparagine
    'AAT': 'N',    # Asparagine
    'AAA': 'K',    # Lysine
    'AAG': 'K',    # Lysine
    'AGC': 'S',    # Serine
    'AGT': 'S',    # Serine
    'AGA': 'R',    # Arginine
    'AGG': 'R',    # Arginine
    'GTA': 'V',    # Valine
    'GTC': 'V',    # Valine
    'GTG': 'V',    # Valine
    'GTT': 'V',    # Valine
    'GCA': 'A',    # Alanine
    'GCC': 'A',    # Alanine
    'GCG': 'A',    # Alanine
    'GCT': 'A',    # Alanine
    'GAC': 'D',    # Aspartic Acid
    'GAT': 'D',    # Aspartic Acid
    'GAA': 'E',    # Glutamic Acid
    'GAG': 'E',    # Glutamic Acid
    'GGA': 'G',    # Glycine
    'GGC': 'G',    # Glycine
    'GGG': 'G',    # Glycine
    'GGT': 'G'     # Glycine
    }
    return codontab
