# Modeling Random Genomes
# construct a random genome based on the CG-content

import math

# every base is independent , so just multiple prob of each base 
def get_probability( seq:str , CG_prob:float ) -> float:
    res_prob = 1
    for i in seq:
        if i == 'A' or i=='T':
            res_prob *= (0.5-CG_prob/2)
        else:
            res_prob *= CG_prob/2
    
    return math.log10(res_prob)

# seq = 'ACGATACAA'
# probs = map( float ,'0.129 0.287 0.423 0.476 0.641 0.742 0.783'.split() )
seq = 'ACATTTCCTGTTCGACAGTCCGCGGTATATAAATTCTCATGTTAGCCATCCCACAAGGACCGAACGCATCGAATCAATCCCTGGGCATAATATAGAGTA'
probs = map( float ,'0.100 0.131 0.182 0.204 0.253 0.304 0.384 0.435 0.459 0.525 0.594 0.631 0.657 0.708 0.769 0.846 0.850 0.941'.split() )

for i in probs:
    print( '%.3f'%( get_probability(seq=seq,CG_prob=i) ) , end= ' ')