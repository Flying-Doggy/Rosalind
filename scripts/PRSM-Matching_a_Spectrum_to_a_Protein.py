# Matching a Spectrum to a Protein

from self_database import amino_mass_table
import collections

def read_PRSM_file( file_path:str ):
    with open( file= file_path ) as f:
        datas = f.readlines()
        n = int(datas[0])
        prots = []
        for i in datas[1:1+n] :
            prots.append( i.strip() )
        specs = []
        for i in datas[1+n:]:
            specs.append( float(i.strip()) )
    return prots , specs

def prot_to_complete_spectrum( prot_seq:str ):
    tmp_spec = set()
    prev = 0
    for i in prot_seq:   # calculate sum of all prefix
        prev += amino_mass_table[i]
        tmp_spec.add( round(prev,5) )
    for i in prot_seq:   # calculate sum of all suffix
        prev -= amino_mass_table[i]
        tmp_spec.add( round(prev,5) )
    return tmp_spec

def Minko_diff( spec_1, sepc_2 ):   # calculate the Minkowski difference  of two specs 
    cnt_dic = collections.defaultdict(int)
    for i in spec_1:
        for j in sepc_2:
            cnt_dic[ round( i-j , 5) ] += 1
    
    tmp_max = 0
    for tmp_dif,tmp_cnt in cnt_dic.items():
        if tmp_cnt > tmp_max:
            tmp_max = tmp_cnt
            res_dif = tmp_dif
    return tmp_max, res_dif

file_path = 'd:/my_blog/github/Rosalind/test_data/PRSM_sample.txt'
prots, query_spec = read_PRSM_file( file_path= file_path )

res_max = 0
res_prot = []
for i in prots:    #compare protein with given spectrum one by one 
    tmp_spec = prot_to_complete_spectrum( i )
    tmp_max,tmp_dif = Minko_diff( tmp_spec , query_spec)
    if tmp_max > res_max:
        res_max = tmp_max
        res_prot = [ i ]
    elif tmp_max == res_max:
        res_prot.append( i )

print( res_max )
print( *res_prot )