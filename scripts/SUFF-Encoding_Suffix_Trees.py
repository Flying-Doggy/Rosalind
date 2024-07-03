# Encoding Suffix Trees
# get all suffix sequences and according to the common prefix to split all suffix

import collections

query = 'ACGATAGCGAGCTTTAAACAACAAAGGATACTCGCATGCTGCAAATCTACGCACGAAGGTTGCAGCAATTCTGTGCTATCGAAGACAGCCCAACAACAAGTAGGATTACAGCAAGGGCCGTAGAAATATGTAAACTGTACAAATGATCATTAAAGAACGAAGTATGTAAACGCGATGTCCCGGCATGCATGTTATGCGCGGTTACACAGGGACAACCCATCACGAGTCTCTTGAAGAATGAATGCGGCGTCTCACGGAATCATTGTGAACGCCGTGGGTCGTTACCTAGGAACCCACGGTCTAGTGGTCACAATTAACGTGCTCTCGTAATTTGAGTGTTTGGCTGTAGTCGCAGTCAGTTCGACATGAGGGTTTCTAGCATCTGCCGCTCCCTGGCTGGACATTGTGACTTAAATCTACCATTGACTAGAATGTGGCCATACGCTAGGTGTTGAGTAGCATTGGATTAACCGCTCCACCCTCTATATCTCAAGTGCAGGCCTTCTGTGCTCGTCAAGTCTTAAACACCGTAGTTCAAGGAAAGCACCTCTGCTTGATTAACAGCCTGACATTCTACGTTTAACACAGGAACGGCCAAGAAGCGCAGCGCGGGTACGGGAGAACACACATGTGGTCCAGAATTCGTATCACACCGACAGAAATTACCCTCTACGCTAACAGAGGGAAGCTGCGCTCCCTATATGCCAAATCGGTCCTTTCAAATATTCACGTCTTCGCGGGCGTACTTATAATGGTAACTTATCGGTCTAGCTCTGGGCTATCGACACCCGGTACTTTGTTTCCGG$'

suffix = []
for i in range( len(query) ):
    suffix.append( query[i:] )

def split_suffix_list( seqs:list , prev = '' ):
    tmp_dic = collections.defaultdict( list )
    if len(seqs) == 1:
        print( prev + seqs[0] )
        return None
    
    for i in seqs:
        tmp_dic[ i[0] ].append( i[1:] )
    
    if len(tmp_dic) == 1:
        for i,next_suf in tmp_dic.items():
            split_suffix_list( next_suf , prev= prev+i )   # the common edge can be get longer
    else:
        if prev:
            print( prev )    # at this index, string has two different characters, common edge's continuity was broken
        for i,next_suf in tmp_dic.items():
            split_suffix_list( next_suf , prev= i )

    return None

split_suffix_list( seqs=suffix , prev= '' )