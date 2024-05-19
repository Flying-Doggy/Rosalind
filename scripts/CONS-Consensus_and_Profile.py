#Consensus and Profile
import collections
from self_database import read_fa_file

file = "D:/rosalind_gc.txt"
fa_dic = read_fa_file( file )

site_dic = [ collections.defaultdict(int) for i in list(fa_dic.values())[0] ]
for tmp_seq in fa_dic.values():
    for idx in range( len(tmp_seq) ):
        site_dic[idx][ tmp_seq[idx] ] += 1

consesus= []
consensus_dic = { 'A':['A:'],'C':['C:'],'G':['G:'],'T':['T:']}
for idx in range( len(tmp_seq) ):
    tmp_max_s = ''
    tmp_max_val = 0
    for tmp_base in ['A','T','C',"G"]:
        consensus_dic[tmp_base].append( site_dic[idx][tmp_base] )
        if site_dic[idx][tmp_base] > tmp_max_val:
            tmp_max_s =tmp_base
            tmp_max_val = site_dic[idx][tmp_base]
    consesus.append( tmp_max_s )
print( ''.join(consesus) )

for i in ['A', 'C', 'G' , 'T']:
    print( ' '.join( [str(j) for j in consensus_dic[i] ] ))