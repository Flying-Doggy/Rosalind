# Global Alignment with Constant Gap Penalty
# the scripts may be similar to GLOB(?)
# we need to discuss the situation of long gaps?

from self_database import BLOSUM62_map,read_fa_file
from math import inf

def two_seq_score_constant_gap( s1:str , s2:str , gap:int = -5 ) -> int:
    cur = [ (gap*(i>0), -inf , -inf ) for i in range(len(s1)+1) ]    
    ## every site has two state gap and non-gap , 1. s2 gap; 2. s1 gap 3.non-gap

    for tmp_s2 in s2:
        # print( cur )
        last, cur = cur , [ ]
        cur.append( (-inf , gap, -inf ) )
        for idx in range(1, len(last) ):
            # no_gap must be generated from diagonal element , just get the biggest score
            no_gap_score = max( last[idx-1] )+ BLOSUM62_map[tmp_s2][s1[idx-1]]

            # two states of gap comes from two points respectively, and discuss their previous state
            up_gap_score = max( cur[-1][0]+gap , cur[-1][1] , cur[-1][2]+gap  )
            left_gap_score = max( last[idx][0], last[idx][1]+gap  , last[idx][2]+gap )
            
            cur.append( (left_gap_score , up_gap_score , no_gap_score))

    return cur[-1]

file_path = 'd:/my_blog/github/Rosalind/test_data/GCON_sample.txt'
s1,s2 = read_fa_file(file_path= file_path , outfmt='list')

print( max(two_seq_score_constant_gap(s1=s1 , s2=s2) ) )

