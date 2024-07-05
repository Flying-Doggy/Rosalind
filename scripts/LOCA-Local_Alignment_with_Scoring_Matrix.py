# Local Alignment with Scoring Matrix
# because the local alignment can skip substrings, so for dp(i,j) = max( dp(i-1,j)+gap , dp(i,j-1)+gap , dp(i-1,j-1)+map_score , 0) ,
# in which 0 means skip all previous substring.

from self_database import PAM250_map,read_fa_file

def two_seq_score( s1:str , s2:str , gap:int = -5 ) -> int:
    cur = [ gap*i for i in range(len(s1)+1) ]

    for tmp_s2 in s2:
        last, cur = cur , [ ]
        cur.append( last[0] + gap )
        for idx in range(1, len(last) ):
            cur.append( max( last[idx]+gap , cur[-1]+gap , last[idx-1]+PAM250_map[tmp_s2][s1[idx-1]] ) )
    
    return cur[-1]


def two_seq_local_align_all( s1:str , s2:str , gap:int = -5 ) -> int:
    # this version can list all max_score substrings paired
    max_score = 0
    max_seq = set()
    cur = [ [0 ,  set( [("" , "")]) ] for i in range(len(s1)+1) ]
    for tmp_s2 in s2:
        last, cur = cur , [ ]
        cur.append( [0 ,  set( [("" , "")]) ] )   # the first one must be 0 to avoid gap penalty
        for idx in range(1, len(last) ):
            up_score = last[idx][0]+gap
            left_score = cur[-1][0] + gap
            dia_score = last[idx-1][0]+PAM250_map[tmp_s2][s1[idx-1]]
            tmp_max = max( up_score , left_score, dia_score )
            if tmp_max <= 0:
                cur.append( [0 ,  set( [("" , "")]) ])
            else:
                cur.append( [ tmp_max, set() ])
                if dia_score == tmp_max:
                    for i1,i2 in last[idx-1][1]:
                        cur[-1][1].add( ( i1+s1[idx-1], i2 + tmp_s2  ) )
                
                if up_score == tmp_max:
                    for i1,i2 in last[idx][1]:
                        cur[-1][1].add( ( i1, i2 + tmp_s2  ) )
                
                if left_score == tmp_max :
                    for i1,i2 in cur[-2][1]:
                        cur[-1][1].add( ( i1 +s1[idx-1], i2  ) )

                if tmp_max > max_score:
                    max_seq =  cur[-1][1] 
                    max_score = tmp_max
                elif tmp_max == max_score:
                    max_seq |= cur[-1][1] 
    
    return max_score,max_seq


def two_seq_local_align( s1:str , s2:str , gap:int = -5 ) -> int:
    max_score = 0
    max_seq = []
    cur = [ (0 , "" , "" )  for i in range(len(s1)+1) ]
    for tmp_s2 in s2:
        last, cur = cur , [ ]
        cur.append( ( 0 , "" , "") )   # the first one must be 0 to avoid gap penalty
        for idx in range(1, len(last) ):
            up_score = last[idx][0]+gap
            left_score = cur[-1][0] + gap
            dia_score = last[idx-1][0]+PAM250_map[tmp_s2][s1[idx-1]]
            tmp_max = max( up_score , left_score, dia_score )
            if tmp_max <= 0:
                cur.append( (0, "", "") )
            else:
                if dia_score == tmp_max:
                    cur.append( ( tmp_max , last[idx-1][1]+s1[idx-1], last[idx-1][2]+ tmp_s2  ) )
                elif up_score == tmp_max:
                    cur.append( ( tmp_max , last[idx][1] , last[idx][2]+ tmp_s2  ) )
                else:
                    cur.append( ( tmp_max , cur[-1][1]+s1[idx-1] , cur[-1][2] ) )
                
                if tmp_max >= max_score:
                    max_seq = [ cur[-1][1:] ]
                    max_score = tmp_max

    return max_score,max_seq

file_path = 'd:/my_blog/github/Rosalind/test_data/LOCA_sample.txt'
s1,s2 = read_fa_file(file_path= file_path , outfmt='list')
score, seqs = two_seq_local_align(s1 , s2)

print( score )
for i,j in seqs:
    print( "%s\n%s"%(i,j))
    print( two_seq_score(i,j) )


