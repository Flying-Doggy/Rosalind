# Finding a Spliced Motif
# it's a simple problem to find substring

from self_database import read_fa_file

fa = read_fa_file('d:/my_blog/github/Rosalind/test_data/SSEQ_sample.txt' , outfmt='list')



# seq_s = 'ACGTACGTGACG'
# seq_t = 'GTA'
seq_s,seq_t = fa

s_idx,t_idx= 0,0

while t_idx < len(seq_t):
    if seq_s[s_idx] == seq_t[t_idx]:
        t_idx += 1
        print( s_idx+1  , end= ' ')
    s_idx += 1
    