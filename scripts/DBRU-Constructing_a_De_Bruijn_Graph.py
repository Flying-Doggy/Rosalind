# Constructing a De Bruijn Graph
from self_database import DNA_rev_comp

def read_DBRU_file( file_path:str )-> list:
    res = []
    with open(file=file_path) as f:
        datas = f.readlines()
        for i in datas:
            res.append( i.strip() )
    return res

def build_de_bruijn( seqs:list ) -> set:
    edges = set()
    for i in seqs:
        edges.add( (i[:-1] ,i[-1]) )
        i = DNA_rev_comp(i)
        edges.add( (i[:-1] ,i[-1]) )
    return edges

file_path = 'd:/my_blog/github/Rosalind/test_data/DRBU_sample.txt'
seqs= read_DBRU_file( file_path= file_path )
graph_DB = build_de_bruijn( seqs= seqs )
for i in sorted(graph_DB):
    print('(%s, %s)'%(i[0] , i[0][1:]+i[1]))