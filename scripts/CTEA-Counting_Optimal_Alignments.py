# Counting Optimal Alignments
# the problem is supposed to be solved by dynamic programing
# dp[i,j] = dp[i-1,j] + dp[i,j-1] + dp[i-1,j-1]

from self_database import read_fa_file

def cnt_optimal_align( s1:str , s2:str ) -> int:
    cur = [ (i,1) for i in range(len(s1)+1)  ]    # ( distance, counts )
    for tmp_s2 in s2:
        last, cur = cur , []
        cur.append( (last[0][0]+1 , 1 ) )     # the first item must be gap 
        for idx in range(1 , len(last) ):
            left_dis, left_cnt = cur[-1]
            up_dis, up_cnt = last[idx]
            dia_dis, dia_cnt = last[idx-1]

            # update cur edit distance from different mapping
            left_dis += 1
            up_dis += 1
            dia_dis += ( tmp_s2 != s1[idx-1] )

            # sum the number of minimum_distance alignments
            tmp_min = min( left_dis, up_dis ,dia_dis )
            tmp_cnt = 0
            if left_dis == tmp_min:
                tmp_cnt += left_cnt
            if up_dis == tmp_min:
                tmp_cnt += up_cnt
            if dia_dis == tmp_min:
                tmp_cnt += dia_cnt
            cur.append( (tmp_min , tmp_cnt ) )
    
    return cur[-1]

MOD= 134217727
file_path = 'd:/my_blog/github/Rosalind/test_data/CTEA_sample.txt'
s1, s2 = read_fa_file( file_path=file_path , outfmt='list' )
print( cnt_optimal_align(s1=s1 , s2= s2)[1]%MOD )
