def to_rna(dna):
    '''
    Given a DNA strand, its transcribed RNA strand is formed
    by replacing each nucleotide with its complement:
    '''

    complement = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'}

    '''
    Make sure imputs are valid DNA nucleotides 
    '''

    for x in dna:
        if x not in ['G', 'C', 'T', 'A']:
            return ''

    return ''.join(complement[nucleotide] for nucleotide in dna)