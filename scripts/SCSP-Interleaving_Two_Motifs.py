# Interleaving Two Motifs
# allowing for the motif to be split onto multiple exons in the process.
# Motifs can be splited into different part!

# seq1 = 'ATCTGAT'
# seq2 = 'TGCATA'
seq1 = 'CGCCCAGACAGGGCGGCGTCTGTGGCGCCGCCGGTCAAGCATCAAGATTTGTTAAGACAAATACTCGGGCGCAGGCACGA'
seq2 = 'GTGATTCTCCCAACCCGATCCCTAGAGTCTCGGGACCACTCGGACTAAGATCCAGAGTTTTAGATCCCCGACTGAAAAGGCTACGGTCTGAAC'

def generate_interleaving_sequence( s1:str , s2:str ):
    cur = [ '' ]
    for i in s1:
        cur.append( cur[-1]+i  )
    
    for j in s2:
        last, cur = cur , [ ]
        for idx in range( len(last) ):
            if idx == 0:
                cur.append( last[0]+ j)
            else:
                a = cur[idx-1] + seq1[idx-1]
                b = last[idx] + j
            
                if j == seq1[idx-1]:
                    c = last[idx-1] +j
                else:
                    c= last[idx-1] +j+seq1[idx-1]
                
                cur.append( sorted([a,b,c] ,key=lambda x:len(x))[0] )
    
    return cur[-1]

print( generate_interleaving_sequence(seq1 , seq2) )