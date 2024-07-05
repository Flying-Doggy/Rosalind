# Genome Assembly Using Reads
# this question is quite similar to PCOV, but the reads may be in reverse-complement and the number of reads are uncomplete.

# My scripts is inspired by https://github.com/Davo36/Rosalind/blob/master/078_GASM.py

# Well, I still have some questions about this problem.
# How to deal with k-mers that highly similar and then the graph path is not unqiue.
# for example, we have these 15-mers 'ATACGACACAGACAGA' 'ATACGACACAGACAGT' 'ATACGACACAGACAGG', and their first 14-base are identical
# when we get 'NATACGACACAGACAG' as previous 15-mer, how to choose one of above three?

# I want to use DFS and Backtracking to search one by one,
# but raise ERROR: maximum recursion depth exceeded while calling a Python object
from self_database import DNA_rev_comp
import collections

def read_GASM_file( file_path:str ) -> list:
    with open( file= file_path ) as f:
        seqs = [ i.strip() for i in f.readlines() ]
    return seqs

def generate_k_mers( seqs:list , k:int ):
    k_mers = []
    for i in seqs:
        for j in range( len(i)-k+1 ):
            k_mers.append( i[j:j+k] )
            k_mers.append( DNA_rev_comp(i[j:j+k]) )
    return list(set(k_mers))

def buid_de_bruijn_graph( seqs:list ):  # use idx tuple to compose an edge
    graph_dic = collections.defaultdict( list )
    prefix_dic = collections.defaultdict( list )
    for idx,s in enumerate( seqs ):
        prefix_dic[ s[:-1] ].append( idx )
    for idx,s in enumerate( seqs ):     
        graph_dic[ idx ] = prefix_dic[ s[1:] ][0]
    return graph_dic

def buid_de_Bruijn( kmers:list , graph_dic:dict ):
    res = []
    visited = set()
    cur = 0
    for i in range(2):    # the question have mentioned exactly two directed cycles. So just test for twice
        while cur in visited:   # get a non-visited node to find cycle.
            cur += 1
        visited.add( cur )
        tmp_seq = kmers[cur][-1]

        next_node = graph_dic.get(cur)
        while next_node != None and next_node not in visited:
            visited.add( next_node )
            tmp_seq += kmers[next_node][-1]
            next_node = graph_dic.get(next_node)
        res.append( tmp_seq )
    
    if len(visited) == len(kmers):
        return res
    else:
        return None

    # # dfs raise ERROR: maximum recursion depth exceeded while calling a Python object
    # def dfs( cur_node:int , start_node:int ):
    #     if start_node == graph_dic[cur_node]:
    #         return ''
    #     next_node=graph_dic[cur_node]
    #     if next_node in visited:
    #         return None
    #     else:
    #         visited.add( next_node )
    #         tmp_res = dfs( next_node , start_node=start_node )
    #         if tmp_res == None:
    #             visited.remove(next_node)
    #             return None
    #         else:
    #             return tmp_k_mers[cur_node][-1]+tmp_res
        
    
    # visited = set()
    # res = []
    # for i in graph_dic.keys():
    #     if i in visited:
    #         continue
    #     else:
    #         visited.add(i)
    #         if ( tmp_res:=dfs(i,i) ):
    #             res.append( kmers[i][-2]+tmp_res )
    # if len(visited) == len(kmers):
    #     return res
            

file_path = 'd:/my_blog/github/Rosalind/test_data/GASM_sample.txt'
seqs = read_GASM_file( file_path=file_path) 
for tmp_k in range( 6,len(seqs[0])-1  ):
    tmp_k_mers = generate_k_mers( seqs= seqs , k=tmp_k )
    tmp_graph = buid_de_bruijn_graph( tmp_k_mers )
    res = buid_de_Bruijn( kmers=tmp_k_mers , graph_dic=tmp_graph) 
    if res:
        print( res[0] )
        break
