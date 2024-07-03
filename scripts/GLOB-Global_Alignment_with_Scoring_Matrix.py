# Global Alignment with Scoring Matrix
# the solution is similar to edit distance, but the distance was replaced by score

from self_database import BLOSUM62_map,read_fa_file

def two_seq_score( s1:str , s2:str , gap:int = -5 ) -> int:
    cur = [ gap*i for i in range(len(s1)+1) ]

    for tmp_s2 in s2:
        last, cur = cur , [ ]
        cur.append( last[0] + gap )
        for idx in range(1, len(last) ):
            cur.append( max( last[idx]+gap , cur[-1]+gap , last[idx-1]+BLOSUM62_map[tmp_s2][s1[idx-1]] ) )
    
    return cur[-1]

file_path = 'd:/my_blog/github/Rosalind/test_data/GLOB_sample.txt'
s1,s2 = read_fa_file(file_path= file_path , outfmt='list')

print( two_seq_score(s1=s1 , s2=s2))