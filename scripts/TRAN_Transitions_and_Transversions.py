#Certain Point Mutations are More Common
# transition: the conversion of A and G , C and T
# tranversion the conversion of A and C,T , G and T,C

from self_database import read_fa_file
import collections

trans_dic = {}
for i in ['A', 'T' , 'C' ,'G']:
    for j in ['A', 'T' , 'C' ,'G']:
        if i==j:
            trans_dic[(i,j)] = 'No_change'
        else:
            trans_dic[(i,j)] = 'tranversion'
trans_dic[ ('A','G') ] = trans_dic[ ('G','A') ]  = trans_dic[ ('C','T') ]  =trans_dic[ ('T','C') ]  ='transition'

def trans_stat( s1:str , s2:str ) -> tuple[int,int] :
    if len(s1) != len(s2):
        print( 'given two sequences are not equal length')
        return [0,0]
    else:
        cnt_dic = collections.defaultdict(int)

        for i in range( len(s1) ):
            tmp_stat = trans_dic[ (s1[i],s2[i]) ]
            cnt_dic[tmp_stat] += 1
        return [cnt_dic['transition'], cnt_dic['tranversion'] ]

fa = read_fa_file( 'd:/my_blog/github/Rosalind/test_data/TRAN_sample.txt' , outfmt='list' )
trans, tranv = trans_stat( fa[0], fa[1] )

print( trans/tranv)