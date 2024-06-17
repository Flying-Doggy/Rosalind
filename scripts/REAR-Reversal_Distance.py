# Reversal Distance
# get the minimum number of reversals required to transform π into σ

# find the mimun group of another (reversal) seq , in which all elements are subsequence of subject seq.
from collections import deque

def read_REAR_file( file_path:str ) -> list:
    res = []
    with open( file= file_path ) as f:
        datas = f.readlines()
        for i in range( 0 , len(datas) , 3 ):
            res.append( tuple( [tuple(datas[i].split()) , tuple(datas[i+1].split()) ] ))
    return res


# on the other hand, we can search the result from seq1 and seq2 at simultaneously.
# catch the time of loop when this two results overlap same sequence.
def min_reversal_dis( seq1:str , seq2:str , cnt_dic:dict ):
    if seq1 == seq2:
        return 0
    tmp_seqs = deque( [seq1] )
    while tmp_seqs:
        tmp_s = tmp_seqs.popleft()
        for i in range( len(seq1) ):    # enumerate reversals one by one to find all possible block orders of tmp_s
            for j in range( i+1, len(seq1) ):
                new_s = tmp_s[:i] + tmp_s[i:j+1][::-1] + tmp_s[j+1:]
                if cnt_dic.get(new_s) != None:   # this ordered block has appeared. So just skip it
                    continue
                cnt_dic[new_s] = cnt_dic[tmp_s] + 1
                if new_s == seq2:
                    return cnt_dic[new_s]
                
                tmp_seqs.append( new_s )


file_path = "d:/my_blog/github/Rosalind/test_data/REAR_sample.txt"
fa_pairs = read_REAR_file( file_path= file_path )

for i,j in fa_pairs:
    print( min_reversal_dis(i,j , {i:0}) , end = ' ')


