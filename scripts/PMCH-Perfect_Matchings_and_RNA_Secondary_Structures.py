# the same number of occurrences of 'A' as 'U' 
# so we just multiple the combination of AU and CG
import math

# Rosalind example
# >Rosalind_5546
# AAUAUUAUCCCGCCGGCCAUGUGACAGAAUAUCGGACUUUAGAGCCAUUGUGGGUCUUUC
# AUCAACGCGCGAGA

query_s = 'AAUAUUAUCCCGCCGGCCAUGUGACAGAAUAUCGGACUUUAGAGCCAUUGUGGGUCUUUCAUCAACGCGCGAGA'

AU_pairs =  query_s.count('A')
CG_pairs = query_s.count('C')

res = 1

# this part can be replaced by `math.factorial( AU_pairs )* math.factorial(CG_pairs)`
for i in range(1,AU_pairs+1):
    res *= i
for i in range(1,CG_pairs+1):
    res *= i

print( res )

