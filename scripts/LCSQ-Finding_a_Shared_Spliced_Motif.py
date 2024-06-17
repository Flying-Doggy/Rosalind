# Finding a Shared Spliced Motif 

# the first idea is to use dp to find out longest common subseq

from self_database import read_fa_file
import collections

file_path = 'd:/my_blog/github/Rosalind/test_data/LCSQ_sample.txt'
fa1 , fa2 = read_fa_file( file_path= file_path , outfmt='list' )


def find_longest_common( seq1:str , seq2:str ) -> list :
    dp = collections.defaultdict( str )

    for i in range( len(seq1) ):
        for j in range( len(seq2) ):
            # dialog matched
            tmp_prev = dp.get( (i-1,j-1) ,"" )
            if seq1[i] == seq2[j]:
                tmp_prev += seq1[i]
            
            # all possible matching schemes
            tmp_prev = sorted( [tmp_prev ,dp.get( (i,j-1), "" ), dp.get( (i-1,j) ,"" )] , key=lambda x:len(x))[-1]

            # find current longest subsequence
            # update dp
            dp[(i,j) ] = tmp_prev

    return dp[ (len(seq1)-1 , len(seq2) - 1 )]

print( find_longest_common(fa1 ,fa2))


## the below script can run all possible longest subsequence, but it need too much memory for 1kbp length

# def find_longest_common( seq1:str , seq2:str ) -> list :
#     dp = collections.defaultdict( set )

#     for i in range( len(seq1) ):
#         for j in range( len(seq2) ):
#             # dialog matched
#             tmp_prev = dp.get( (i-1,j-1) , set( [""]) )
#             if seq1[i] == seq2[j]:
#                 tmp_prev = set( [ k+seq1[i] for k in tmp_prev] )
            
#             # all possible matching schemes
#             tmp_prev = tmp_prev | dp.get( (i,j-1) , set( [""]) ) | dp.get( (i-1,j) , set( [""]) )

#             # find current longest subsequence
#             max_len = max( [len(i) for i in tmp_prev ] )
#             tmp_prev = set( [i for i in tmp_prev if len(i)== max_len] )

#             # update dp
#             dp[(i,j) ] = tmp_prev
#     return dp[ (len(seq1)-1 , len(seq2) - 1 )]

# pop one seq of result to match request of problem
# print( find_longest_common(fa1 ,fa2).pop() )

            
            


