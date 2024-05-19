#Open Reading Frames
import re
from self_database import DNA_codon_map,DNA_rev_comp

def DNA_to_prot( dna_seq:str ) -> str:
    
    prot_seq = ''
    for idx in range( 0,len(dna_seq),3):
        prot_seq += DNA_codon_map.get( dna_seq[idx : idx + 3 ] )
        if prot_seq[-1] == '*':
            break
    return prot_seq[:-1]

def find_uni_ORF( DNA_seq:str ) -> list:
    orf_list = []
    starts = [ ]
    stops = []
    for i in range( len(DNA_seq)-3 ):
        if DNA_seq[i:i+3] == 'ATG':
            starts.append( i )
        elif DNA_codon_map.get( DNA_seq[i:i+3]  ) == '*':
            stops.append( i )
    #print( starts , stops)
    
    for tmp_start in starts:
        for tmp_stop in stops:
            if tmp_stop-tmp_start > 0 and (tmp_stop-tmp_start)%3 == 0:
                orf_list.append( DNA_to_prot( DNA_seq[tmp_start:tmp_stop+3] ) )
                break
    
    return orf_list

def find_dual_ORF( seq:str ) -> list:
    rc_seq = DNA_rev_comp( seq )
    orfs = set( find_uni_ORF(seq) + find_uni_ORF(rc_seq) )
    return orfs

seq = "CCGGGGAGCTGGCACAACAGGATCGCGCGAATCTACTGGTAATTCCAACCCGACCCGGTTGTTCATAGGAGGGCGTGTAACCAAATAAAGAATGATCTAGCCGACCAAGGTTGAGTTACTAATATACGTGAAAGGGACGTAACTAAGGAGAAGCCGCGTTAATAAGGATCTCGATTAGAGTAAGTCGGCTGGAAGGAAATCATGAGTTCCTTCCACTCGCTCTGGTTACGGCGAAATTGCGCCATTTTGGATTTCGGAAAAATACCCTTTTGGGCCTTCTCCGATAATGCTTGAGGTTTATATAGGTACACCTCCCATTCGTTGCCGTCAATCATTACGCTTACAGTTCGACGTGATTTGTCTTTATCTCCTAGAGTCCAGCGATTGGAGGGTCCCATTCTACCCCCAGTTGGTCATGAATGCGAATTAATGCCGTGGCGCAGCCTGCAGACTAATCCGGCATAGCTATGCCGGATTAGTCTGCAGGCTGCGCCACGGCATGCGTCGGCGATGCCCTGACAAAGAAACCGTGGTTACAATGTATCGCTCTCAGAAACGCTAGGAGTACCTTGCGCTGAGATCGACAGTACCTAACACTAACTCCTAATTGATCTATAATATTGGGGACATACCCGTAGAGACCCTACAGTAGTAGACGCGTTTTCAATCTACCAGTATCCAATGTGGCGCATGTGAAAGGTTCACGGGTTAAAATCCTTAACGATGGGGGTGTGCCAGAATTTGATAAAGCCACAAACTCCCCAAGGGACCGGCGCGGCCCAGATGTACGGTTTAGAGAGTCTATCAGGTATGGCTGTCTCCACGTATGATAGGCGAGCCCTCGGCCTAGCATAAAGCAGCAATGACACCTGAACTACACGCTCAGCCCATGCCTCACGCGTTGGTGCGGTGGTTAGGTGGAGGGACACT"
orfs = find_dual_ORF( seq=seq)
for i in orfs:
    print(i)