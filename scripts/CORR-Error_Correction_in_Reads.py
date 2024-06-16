# Genome Sequencing Isn't Perfect
# Error Correction in Reads
# we need to screen all seqs twice, first to find out correct sequence, second to correct false reads

from self_database import read_fa_file,DNA_rev_comp

def dis( seq1:str ,  seq2:str) -> int:
    return sum( [seq1[i] != seq2[i] for i in range(len(seq1))] ) 

file_path = 'd:/my_blog/github/Rosalind/test_data/CORR_sample.txt'
fa_list = read_fa_file( file_path=file_path , outfmt='list' )

cnt_dic = {}
for i in fa_list:
    rv_i = DNA_rev_comp(i)
    if cnt_dic.get(i) == None and cnt_dic.get(rv_i) == None:
        cnt_dic[i] = 1
    elif cnt_dic.get(i):
        cnt_dic[i] += 1
    else:
        cnt_dic[ rv_i ] += 1 

correct = [ ]
incorrect = []
for i in cnt_dic.keys():
    if cnt_dic[i] >= 2:
        correct.append( i )
        correct.append( DNA_rev_comp(i) )
    else:
        incorrect.append( i )


for i in incorrect:
    rv_i = DNA_rev_comp(i)
    for j in correct:
        if dis( i,j )== 1:
            print( "%s->%s"%(i,j) )
            break


