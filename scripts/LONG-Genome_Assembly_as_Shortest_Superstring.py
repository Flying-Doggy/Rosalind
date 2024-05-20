#Genome Assembly as Shortest Superstring
from self_database import read_fa_file
import collections
import time

# this script can assembly 50 reads each length of 1000 bp in 0.01 seconds.
# script applys methods like set paired limitation, update merged reads simultaneously, cut used reads ... to reduce steps

file_path = "D:/rosalind_gc.txt"
fa_dic = read_fa_file( file_path= file_path )

def overlapping_seqs( seq1:str , seq2:str , ratio:float=0.5 , lim_length:int=5 , lim_flag:str = 'len'):
    # to identify seq1 is link after seq2
    if lim_flag == 'len':
        len_limit = lim_length
    else:
        len_limit = ratio*min(len(seq1),len(seq2))
    
    for idx in range( len(seq1) ):
        if len(seq1)-idx > len_limit:    # skip the remain index whose remaining length less than queired limit.
            if seq1[idx] == seq2[0]:
                if seq2.startswith( seq1[idx:] ):
                    return True, seq1[:idx]+seq2
        else:
            break
    return False, "" 

def assembly_iter( seq_dic:dict , cnt_dic:dict , lim_len:int ):
    cnt = flag = 1

    while flag:
        flag = 0
        id_list = list( seq_dic.keys() )
        # one-by-one comparison to find out pairs that can be merged
        for idx1 in range( len(id_list)-1 ):
            for idx2 in range( idx1+1 , len(id_list)):
                tmp_seq1 , tmp_seq2 = seq_dic[ id_list[idx1] ],seq_dic[ id_list[idx2] ]
                ## seq2→seq1
                tmp_flag, tmp_seq = overlapping_seqs( tmp_seq1 , tmp_seq2 , lim_length=lim_len )
                if tmp_flag:
                    flag = 1
                else:
                    ## seq1 → seq2
                    tmp_flag, tmp_seq = overlapping_seqs( tmp_seq2 , tmp_seq1 , lim_length=lim_len )
                    if tmp_flag:
                        flag = 1
                if tmp_flag:    # two reads are overlapped into a new long reads
                    cnt += 1
                    seq_dic[cnt] = tmp_seq
                    cnt_dic[ cnt ] = cnt_dic[ id_list[idx1] ] + cnt_dic[id_list[idx2]]
                    del seq_dic[ id_list[idx1] ]
                    del seq_dic[ id_list[idx2] ]
                    break
            if flag:
                break
    return seq_dic

n = len( list(fa_dic.values())[0] ) 
cnt_dic = collections.defaultdict(int )
for i in fa_dic.keys():
    cnt_dic[i] = 1


# print( assembly_iter(fa_dic , cnt_dic=cnt_dic , lim_len=(n+1)//2 ) )
# print( sorted(cnt_dic.items() , key = lambda x:x[1]) )
