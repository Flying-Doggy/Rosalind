# Genome Assembly with Perfect Coverage

def read_PCOV_file( file_path:str ) -> list:
    with open( file= file_path) as f:
        res = [ i.strip() for i in f.readlines()]
    return res

def get_prefix_deb( seqs:list ) -> dict:
    prefix = {}
    for idx,i in enumerate(seqs):
        prefix[ i[:-1] ] = (idx,i[-1])
    return prefix

file_path = 'd:/my_blog/github/Rosalind/test_data/PCOV_sample.txt'
seqs = read_PCOV_file( file_path= file_path )

prefix = get_prefix_deb( seqs=seqs )
res = ''
tmp_idx = 0
while res== '' or tmp_idx != 0:
    next_idx,next_base = prefix[ seqs[tmp_idx][1:] ]
    res += next_base
    tmp_idx = next_idx 

print( res )