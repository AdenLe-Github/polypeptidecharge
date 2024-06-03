

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
        'CAC': 0,    # Histidine
        'CAT': 0,    # Histidine
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

def codonchartsize():
    codontabsize = {
            'TCA': 89.0,    # Serine
            'TCC': 89.0,    # Serine
            'TCG': 89.0,    # Serine
            'TCT': 89.0,    # Serine
            'TTC': 189.9,    # Phenylalanine
            'TTT': 189.9,    # Phenylalanine
            'TTA': 166.7,    # Leucine
            'TTG': 166.7,    # Leucine
            'TAC': 193.6,    # Tyrosine
            'TAT': 193.6,    # Tyrosine
            'TAA': 0.0,    # Stop
            'TAG': 0.0,    # Stop
            'TGC': 108.5,    # Cysteine
            'TGT': 108.5,    # Cysteine
            'TGA': 0.0,    # Stop
            'TGG': 227.8,    # Tryptophan
            'CTA': 166.7,    # Leucine
            'CTC': 166.7,    # Leucine
            'CTG': 166.7,    # Leucine
            'CTT': 166.7,    # Leucine
            'CCA': 112.7,    # Proline
            'CCC': 112.7,    # Proline
            'CCG': 112.7,    # Proline
            'CCT': 112.7,    # Proline
            'CAC': 153.2,    # Histidine
            'CAT': 153.2,    # Histidine
            'CAA': 143.8,    # Glutamine
            'CAG': 143.8,    # Glutamine
            'CGA': 173.4,    # Arginine
            'CGC': 173.4,    # Arginine
            'CGG': 173.4,    # Arginine
            'CGT': 173.4,    # Arginine
            'ATA': 166.7,    # Isoleucine
            'ATC': 166.7,    # Isoleucine
            'ATT': 166.7,    # Isoleucine
            'ATG': 162.9,    # Methionine
            'ACA': 116.1,    # Threonine
            'ACC': 116.1,    # Threonine
            'ACG': 116.1,    # Threonine
            'ACT': 116.1,    # Threonine
            'AAC': 114.1,    # Asparagine
            'AAT': 114.1,    # Asparagine
            'AAA': 168.6,    # Lysine
            'AAG': 168.6,    # Lysine
            'AGC': 89.0,    # Serine
            'AGT': 89.0,    # Serine
            'AGA': 173.4,    # Arginine
            'AGG': 173.4,    # Arginine
            'GTA': 140.0,    # Valine
            'GTC': 140.0,    # Valine
            'GTG': 140.0,    # Valine
            'GTT': 140.0,    # Valine
            'GCA': 88.6,    # Alanine
            'GCC': 88.6,    # Alanine
            'GCG': 88.6,    # Alanine
            'GCT': 88.6,    # Alanine
            'GAC': 111.1,   # Aspartic Acid
            'GAT': 111.1,   # Aspartic Acid
            'GAA': 138.4,   # Glutamic Acid
            'GAG': 138.4,   # Glutamic Acid
            'GGA': 60.1,    # Glycine
            'GGC': 60.1,    # Glycine
            'GGG': 60.1,    # Glycine
            'GGT': 60.1     # Glycine
        }
    return codontabsize

def codonchartmass():
    codontabmass = {
            'TCA': 105,    # Serine
            'TCC': 105,    # Serine
            'TCG': 105,    # Serine
            'TCT': 105,    # Serine
            'TTC': 165,    # Phenylalanine
            'TTT': 165,    # Phenylalanine
            'TTA': 131,    # Leucine
            'TTG': 131,    # Leucine
            'TAC': 181,    # Tyrosine
            'TAT': 181,    # Tyrosine
            'TAA': 0,    # Stop
            'TAG': 0,    # Stop
            'TGC': 121,    # Cysteine
            'TGT': 121,    # Cysteine
            'TGA': 0,    # Stop
            'TGG': 204,    # Tryptophan
            'CTA': 131,    # Leucine
            'CTC': 131,    # Leucine
            'CTG': 131,    # Leucine
            'CTT': 131,    # Leucine
            'CCA': 115,    # Proline
            'CCC': 115,    # Proline
            'CCG': 115,    # Proline
            'CCT': 115,    # Proline
            'CAC': 155,    # Histidine
            'CAT': 155,    # Histidine
            'CAA': 146,    # Glutamine
            'CAG': 146,    # Glutamine
            'CGA': 174,    # Arginine
            'CGC': 174,    # Arginine
            'CGG': 174,    # Arginine
            'CGT': 174,    # Arginine
            'ATA': 131,    # Isoleucine
            'ATC': 131,    # Isoleucine
            'ATT': 131,    # Isoleucine
            'ATG': 149,    # Methionine
            'ACA': 119,    # Threonine
            'ACC': 119,    # Threonine
            'ACG': 119,    # Threonine
            'ACT': 119,    # Threonine
            'AAC': 132,    # Asparagine
            'AAT': 132,    # Asparagine
            'AAA': 146,    # Lysine
            'AAG': 146,    # Lysine
            'AGC': 105,    # Serine
            'AGT': 105,    # Serine
            'AGA': 174,    # Arginine
            'AGG': 174,    # Arginine
            'GTA': 117,    # Valine
            'GTC': 117,    # Valine
            'GTG': 117,    # Valine
            'GTT': 117,    # Valine
            'GCA': 89,    # Alanine
            'GCC': 89,    # Alanine
            'GCG': 89,    # Alanine
            'GCT': 89,    # Alanine
            'GAC': 133,   # Aspartic Acid
            'GAT': 133,   # Aspartic Acid
            'GAA': 147,   # Glutamic Acid
            'GAG': 147,   # Glutamic Acid
            'GGA': 75,    # Glycine
            'GGC': 75,    # Glycine
            'GGG': 75,    # Glycine
            'GGT': 75     # Glycine
        }
    return codontabmass


def codoncharthydro():
    codontabhydro = {
            'TCA': -0.8,    # Serine
            'TCC': -0.8,    # Serine
            'TCG': -0.8,    # Serine
            'TCT': -0.8,    # Serine
            'TTC': 2.8,     # Phenylalanine
            'TTT': 2.8,     # Phenylalanine
            'TTA': 3.8,     # Leucine
            'TTG': 3.8,     # Leucine
            'TAC': -1.3,    # Tyrosine
            'TAT': -1.3,    # Tyrosine
            'TAA': 0,       # Stop
            'TAG': 0,       # Stop
            'TGC': 2.5,     # Cysteine
            'TGT': 2.5,     # Cysteine
            'TGA': 0,       # Stop
            'TGG': -0.9,    # Tryptophan
            'CTA': 3.8,     # Leucine
            'CTC': 3.8,     # Leucine
            'CTG': 3.8,     # Leucine
            'CTT': 3.8,     # Leucine
            'CCA': -1.6,    # Proline
            'CCC': -1.6,    # Proline
            'CCG': -1.6,    # Proline
            'CCT': -1.6,    # Proline
            'CAC': -3.2,    # Histidine
            'CAT': -3.2,    # Histidine
            'CAA': -3.5,    # Glutamine
            'CAG': -3.5,    # Glutamine
            'CGA': -4.5,    # Arginine
            'CGC': -4.5,    # Arginine
            'CGG': -4.5,    # Arginine
            'CGT': -4.5,    # Arginine
            'ATA': 4.5,     # Isoleucine
            'ATC': 4.5,     # Isoleucine
            'ATT': 4.5,     # Isoleucine
            'ATG': 1.9,     # Methionine
            'ACA': -0.7,    # Threonine
            'ACC': -0.7,    # Threonine
            'ACG': -0.7,    # Threonine
            'ACT': -0.7,    # Threonine
            'AAC': -3.5,    # Asparagine
            'AAT': -3.5,    # Asparagine
            'AAA': -3.9,    # Lysine
            'AAG': -3.9,    # Lysine
            'AGC': -0.8,    # Serine
            'AGT': -0.8,    # Serine
            'AGA': -4.5,    # Arginine
            'AGG': -4.5,    # Arginine
            'GTA': 4.2,     # Valine
            'GTC': 4.2,     # Valine
            'GTG': 4.2,     # Valine
            'GTT': 4.2,     # Valine
            'GCA': 1.8,     # Alanine
            'GCC': 1.8,     # Alanine
            'GCG': 1.8,     # Alanine
            'GCT': 1.8,     # Alanine
            'GAC': -3.5,    # Aspartic acid
            'GAT': -3.5,    # Aspartic acid
            'GAA': -3.5,    # Glutamic Acid
            'GAG': -3.5,    # Glutamic Acid
            'GGA': -0.4,    # Glycine
            'GGC': -0.4,    # Glycine
            'GGG': -0.4,    # Glycine
            'GGT': -0.4     # Glycine
        }
    return codontabhydro