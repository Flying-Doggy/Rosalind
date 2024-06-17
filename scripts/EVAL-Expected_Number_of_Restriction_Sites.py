# Expected Number of Restriction Sites 
# calculate the possiblity of query sequence. and each of DNA sequence is independent ,
# multiple the number of sequences can get the expectation

# n = 10
# query = 'AG'
# CG_ratios = map(float ,'0.25 0.5 0.75'.split())

n = 838769
query = 'CGTGTAGT'
CG_ratios = map(float ,'0.000 0.082 0.145 0.171 0.211 0.289 0.366 0.403 0.450 0.516 0.578 0.603 0.647 0.701 0.752 0.821 0.871 0.926 1.000'.split())



def cal_motif_prob( motif:str , CG_ratio:float ) -> float:
    appear_dic = { 'C':CG_ratio/2 , 'G':CG_ratio/2 , 'A':0.5-CG_ratio/2, 'T':0.5-CG_ratio/2}
    motif_prob = 1
    for i in motif:
        motif_prob *= appear_dic[i]
    
    return motif_prob 

for i in CG_ratios:
    print( cal_motif_prob(query,i)*( n-len(query)+1 )  , end =' ' )