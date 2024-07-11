# Maximizing the Gap Symbols of an Optimal Alignment
# to maximize the number of gap, we can minimize the gap penalty

from self_database import read_fa_file
from collections import defaultdict

def edit_distance_mgap(seq1, seq2 , match_score:int = 5 , mismatch_penalty:int = -10000 , gap_penalty: int = -1): 
    # the output query is the number of gap, so we need a tuple to dynamic programming 
    cur = [ (gap_penalty*i, i) for i in range(len(seq1)+1 ) ]
    for j, s in enumerate(seq2):
        last, cur = cur, [ ]
        cur.append(  (last[0][0]+gap_penalty ,  last[0][1]+1) ) 
        for i, t in enumerate(seq1):
            up_ = ( last[i+1][0] + gap_penalty , last[i+1][1]+1 )
            left_ = ( cur[-1][0] + gap_penalty ,cur[-1][1]+1 )
            dia_ = ( last[i][0] + match_score if s==t else last[i][0] +mismatch_penalty , last[i][1] )
            
            cur.append( sorted([up_ , left_ , dia_])[-1] )

    return cur[-1]

file_path = 'd:/my_blog/github/Rosalind/test_data/MGAP_sample.txt'
s1,s2 = read_fa_file( file_path= file_path , outfmt='list' )
print( edit_distance_mgap(s1,s2)[1] )
