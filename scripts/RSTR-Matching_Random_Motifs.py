# Matching Random Motifs
# in a randomly constructed genome, calculate the possibility to appear a given motif

# genome_n, CG = 90000, 0.6
# motif = 'ATAGCCGA'
genome_n, CG = 92458, 0.597895
motif = 'GGCGTAACA'

def cal_motif_prob( motif:str , genome_size:int , CG_ratio:float ) -> float:
    appear_dic = { 'C':CG_ratio/2 , 'G':CG_ratio/2 , 'A':0.5-CG_ratio/2, 'T':0.5-CG_ratio/2}
    motif_prob = 1
    for i in motif:
        motif_prob *= appear_dic[i]
    
    return motif_prob , 1-pow( 1-motif_prob , genome_size )

print( cal_motif_prob( motif=motif , genome_size=genome_n , CG_ratio=CG) )