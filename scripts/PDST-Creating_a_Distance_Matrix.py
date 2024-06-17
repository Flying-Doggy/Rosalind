# Creating a Distance Matrix
# the distance d(s1,s2) is the proportion of corresponding symbols that differ between s1 and s2. ( Hamming distance )

from self_database import read_fa_file

def hamming( seq1:str , seq2:str ):
    # seq1 and seq2 should be equal length
    if len(seq1) != len(seq2):
        print( "%s and %s are not equal length, please check the input sequence"%( seq1 , seq2 ) )
        return 0
    else:
        mis_cnt = sum( [ seq1[i] != seq2[i] for i in range(len(seq1)) ] )
        return round( mis_cnt/len(seq1) , 6)


file_path = 'd:/my_blog/github/Rosalind/test_data/PDST_sample.txt'
fa_list = read_fa_file( file_path=file_path , outfmt='list' )


res = [ [ 0 for i in fa_list ] for i in fa_list ]
n = len(fa_list)

for i in range(n):
    for j in range(i+1,n):
        tmp_res = hamming( fa_list[i], fa_list[j] )
        res[i][j] = res[j][i] = tmp_res

for i in res:
    print( *i )