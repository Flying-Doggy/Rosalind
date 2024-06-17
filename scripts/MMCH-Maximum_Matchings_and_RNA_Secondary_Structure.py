# Maximum Matchings and RNA Secondary Structures
# this problem is similar to PMCH, the only change is N_A not equal to N_U, N_G not equal to N_C
# So the full permutation problem in PMCH has changed to paritial permutation in this problem

import collections
from math import perm

# seq = 'AUGCUUC'
seq = 'CCAGUUAGCCCGACUGAUACCAGUCGCUCUGUAGGGAACAGUUUGGCGACACACGACCCUCAUCUUAGGGGACGUUCGUAAUUAAAUGAUCGGAG'

base_cnt = collections.defaultdict(int)
for i in seq:
    base_cnt[i] += 1

A_U_pairs = perm( max(base_cnt['A'], base_cnt['U']) , min(base_cnt['A'], base_cnt['U']) )
C_G_pairs = perm( max(base_cnt['C'], base_cnt['G']) , min(base_cnt['C'], base_cnt['G']) )

print( A_U_pairs*C_G_pairs)