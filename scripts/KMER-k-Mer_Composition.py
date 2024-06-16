#k-Mer Composition

from self_database import read_fa_file

file_path = 'D:/my_blog/github/Rosalind/test_data/KMER_sample.txt'
fa = read_fa_file( file_path=file_path , outfmt='list')[0]
k = 4


def generate_k_cnt_dic( k:int ) -> dict :
    cur = [ '' ]
    for i in range(k):
        next_k = []
        for prev in cur:
            for base in ['A' , 'T' , 'C' , 'G']:
                next_k.append( prev+base )
        cur = next_k
    return dict( zip( cur, [0]*len(cur)) )

kmer_cnt_dic = generate_k_cnt_dic( k= k )
for i in range( len(fa)-k+1 ):
    kmer_cnt_dic[ fa[i:i+k] ] += 1

print( *[ i[1]  for i in sorted(kmer_cnt_dic.items() , key=lambda x:x[0])])

