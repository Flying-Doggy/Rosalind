# Independent Segregation of Chromosomes
# 

import math

n = 43
N=2*n
all_pos = 2**(N)
tmp_pos = 0
for i in range( N ):
    tmp_pos += math.comb( N,i) 
    print( round( math.log10( (all_pos-tmp_pos)/all_pos ),3) )   
    #if 1 - tmp_pos/all_pos , the scirpt will raise `domain error` when tmp_pos is big enough beacause of accuracy.


