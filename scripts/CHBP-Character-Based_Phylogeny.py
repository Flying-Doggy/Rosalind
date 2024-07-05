# Character-Based Phylogeny
# because the given character model have NO CONFLIT, we can deduce the tree one by one.
# the script is inspired by https://github.com/danhalligan/rosalind.info/blob/main/rosalind/bioinformatics_stronghold/chbp.py

import collections
def read_CHBP_file( file_path:str ):
    with open(file= file_path ) as f:
        datas = f.readlines()
        species = datas[0].strip().split()
        chars = [ list(i.strip()) for i in datas[1:] ]
    return species, chars

def iter_tree( tree_nodes:list, ref_dic:dict ):
    next_nodes = [ ]
    # use a set to record merged nodes
    visited = set()  
    for i in range( len(tree_nodes) ):
        if i in visited:
            continue
        for j in range( i+1, len(tree_nodes) ):
            if j in visited:
                continue
            next_group = tuple(sorted(tree_nodes[i][0] + tree_nodes[j][0]))
            # print( next_group )
            if next_group in ref_dic[ len(next_group) ]:    # find weather the new group has been included in characters
                next_nodes.append( (next_group, '(%s,%s)'%( tree_nodes[i][1] , tree_nodes[j][1] ) ))
                visited.add(i)
                visited.add(j)
                break
    next_nodes.extend( [ tree_nodes[i] for i in range(len(tree_nodes) ) if i not in visited] )
    
    return next_nodes, len(visited)==0    # the current nodes can't be merged into new parent node: True to break the iteration

def generate_groups( characters:list ) -> dict:
    ref_dic = collections.defaultdict( set )
    for i in chars:
        tmp_0 = [ ] # set is used to keep unique tuple group ( element was sorted by index)
        tmp_1 = [ ]
        
        for idx in range( len(i) ):    # generate group information
            if i[idx] == '1':
                tmp_1.append(idx)
            else:
                tmp_0.append(idx)
        
        if len( tmp_1 ) < len(tmp_0):
            ref_dic[ len(tmp_1) ].add( tuple(tmp_1) )
        # elif len( tmp_1 ) == len(tmp_0):
        #     ref_dic[ len(tmp_0) ].append( tmp_0 )
        #     ref_dic[ len(tmp_1) ].append( tmp_1 )
        else:
            ref_dic[ len(tmp_0) ].add( tuple(tmp_0) )
    return ref_dic


file_path = 'd:/my_blog/github/Rosalind/test_data/CHBP_sample.txt'
species, chars = read_CHBP_file( file_path= file_path)

ref_dic = generate_groups( characters=chars)

nodes = [ ( tuple([i]) , species[i] ) for i in range( len(species) ) ]
while True:
    nodes,flag = iter_tree( nodes, ref_dic=ref_dic )
    if flag :
        break

print( '(%s);'%','.join([i[1] for i in nodes] ) )
