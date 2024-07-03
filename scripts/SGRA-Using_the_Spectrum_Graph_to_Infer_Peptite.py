# Using the Spectrum Graph to Infer Peptides
# just follow the introductions to construct a digraph and then get the longest protein_seq

from self_database import amino_mass_table
import collections

mass_amino_dic = dict( [ [round(i[1],4),i[0]] for i in amino_mass_table.items()])

def read_SGRA_file( file_path:str ) -> list:
    with open(file= file_path ) as f:
        datas = f.readlines()
    return [ float(i) for i in datas ] 

def construct_digraph_pep( specs:list ):
    pep_graph = collections.defaultdict(dict)
    for i in range( len(specs ) ):
        for j in range( i+1 , len(specs) ):
            if mass_amino_dic.get( round( specs[j]-specs[i],4) ):
                pep_graph[i][j] = mass_amino_dic.get(round(specs[j]-specs[i],4))
    return pep_graph

def find_longest( graph:dict , cur:int , visited:dict , amino:str  = '') -> str:   # get all possible longest
    longest_seq = set( [''])
    visited[ cur ] = 1
    for next in graph[cur].keys():
        tmp_seq = find_longest( graph=graph , cur=next , visited=visited, amino= graph[cur][next] )


        a , b = longest_seq.pop() , tmp_seq.pop()
        if len(b) > len(a):
            longest_seq = tmp_seq
            longest_seq.add( b )
        elif len(b) == len(a):
            longest_seq |= tmp_seq
            longest_seq.add(a )
            longest_seq.add(b)
        else:
            longest_seq.add(a )
    
    # add current amino to the return_back peps
    longest_seq = set( [amino+i for i in longest_seq] )
    
    return longest_seq

file_path = 'd:/my_blog/github/Rosalind/test_data/SGRA_sample.txt'
specs = read_SGRA_file( file_path= file_path )
pep_graph = construct_digraph_pep( specs= specs )
visited = [ 0 for i in specs ]

for i in range( len(specs) ):
    if visited[i]:
        continue 
    else:
        a = find_longest(graph=pep_graph , cur= i , visited= visited ).pop()
        if a:   # don't print NONE result
            print(  a , len(a) )

