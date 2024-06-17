# Edit Distance

from self_database import read_fa_file
import collections
import time


file_path = 'd:/my_blog/github/Rosalind/test_data/EDIT_sample.txt'
seq1, seq2 = read_fa_file( file_path= file_path , outfmt='list' )

def edit_dis( s1:str , s2:str ) -> int: # memory each idx pair
    dp = collections.defaultdict( int )
    for i in range( len(s1) ):
        dp[ (i,-1) ] = i+1
    for j in range( len(s2) ):
        dp[ (-1,j) ] = j+1
     
    for i in range( len(s1) ):
        for j in range( len(s2) ):
            dp[ (i,j) ]  = min( dp[(i-1,j)]+1 , dp[(i,j-1)]+1 , dp[(i-1,j-1)] + (s1[i]!=s2[j]) )

    return dp[( i,j )]


def edit_distance(seq1, seq2): # Wagner-Fischer algorithm
    cur = list(range(len(seq1)+1))
    for j, s in enumerate(seq2):
        last, cur = cur, [j+1] 
        for i, t in enumerate(seq1):
            cur.append(last[i] if s==t else min([last[i+1], last[i], cur[-1]]) + 1)
    return cur[-1]


def minDistance( s: str, t: str) -> int:
    f = list(range(len(t) + 1))
    for x in s:
        pre = f[0]
        f[0] += 1
        for j, y in enumerate(t):
            tmp = f[j + 1]
            f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
            pre = tmp
    return f[-1]





print( edit_dis(seq1 , seq2 ))