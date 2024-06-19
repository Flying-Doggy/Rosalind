# # Newick Format with Edge Weights
# # the script is similar to NWCK , modify parse_newick function to get edge of each node

### self-made structure to find nodes'distance
import collections

def read_NKEW_file( file_path:str ) -> list:
    res = []
    with open( file= file_path ) as f:
        datas = f.readlines()
        for i in range( 0, len(datas) ,3 ):
            nwk_tree = datas[i].strip()
            node_pair = datas[i+1].split()
            res.append( (nwk_tree, node_pair ) )
    return res


# class phylo_node:
#     def __init__(self , val:str , n_type:str = None , sons:list = [] , parent = None , brach_length:int=0) -> None:
#         self.val = val
#         self.type = n_type
#         self.s = sons
#         self.branch_len = brach_length
#         self.p = parent
#         pass

#     def get_offsprings( self ):
#         if self.type == 'leaf':
#             return [self.val]
#         else:
#             tmp_res = [ ]
#             for tmp_son in self.s:
#                 tmp_res.extend( tmp_son.get_offsprings() )
#             return tmp_res
    
#     def to_node( self , target:str ) -> int:
#         visited = set( [ self ] )
#         cur = collections.deque( [ ( self, 0 ) ] )
#         while cur:
#             tmp_node,tmp_dis = cur.popleft()
#             # print( tmp_node , tmp_dis)
#             for new_node in tmp_node.s:
#                 if new_node in visited:   # skip the screened node
#                     continue
#                 if new_node.val == target:
#                     return tmp_dis+ new_node.branch_len 
#                 cur.append( (new_node , tmp_dis+ new_node.branch_len ) )
#                 visited.add( new_node )
            
#             if tmp_node.p in visited or tmp_node.p == None:
#                 continue
#             else:
#                 if tmp_node.p and tmp_node.p.val == target:
#                     return tmp_dis+ tmp_node.branch_len 
#                 cur.append( (tmp_node.p, tmp_dis + tmp_node.branch_len ))
#                 visited.add( tmp_node.p )     


#     def __repr__(self) -> str:
#         if self.p == None:
#             return 'self:%s , parent:%s , sons:'%( self.val, "None" ) + str([son.val for son in self.s ])
#         return 'self:%s , parent:%s , sons:'%( self.val, self.p.val ) + str([son.val for son in self.s ])
    

# def parse_nwk( nwk_s:str ) -> dict:
#     phylo_dic = collections.defaultdict( phylo_node )
#     internode_cnt = 0
#     stack = [ '' ]
#     idx = 0
#     while idx < len(nwk_s):
#         if nwk_s[idx] == ',' or nwk_s[idx] == ';' :
#             stack.append( '' )
#         elif nwk_s[idx]  == '(':
#             stack[-1] += nwk_s[idx] 
#             stack.append( '' )
#         elif nwk_s[idx]  == ')':
#             tmp_id = ''
#             while nwk_s[idx+1] != ',' and nwk_s[idx+1] != ';' and nwk_s[idx+1] != ')':
#                 idx += 1
#                 tmp_id += nwk_s[idx]
            
#             if ':' in tmp_id:                       # judge wheather the brach_length exists
#                 tmp_id,tmp_len = tmp_id.split(':')   # because the tree branches have weight
#             else:
#                 tmp_len = 0
            
#             # create a phylo_node to store all sons
#             if tmp_id == '':
#                 tmp_id = internode_cnt
#                 internode_cnt += 1
#             tmp_node = phylo_node( val=tmp_id, n_type='inter' , sons=[] , brach_length= int(tmp_len) )
#             phylo_dic[tmp_id] = tmp_node

#             # get the information of sons
#             tmp_sons = []
#             while stack[-1] != '(':
#                 a = stack.pop()
#                 if a != '':
#                     tmp_sons.append( a ) 
#             stack.pop()
#             stack.append( tmp_node )

#             # connect sons to parent node 
#             for son in tmp_sons:
#                 if type(son) == str:
#                     if ':' in son:
#                         son, son_len = son.split(':')
#                     else:
#                         son_len = 0
#                     son_node = phylo_node( val=son , n_type='leaf' , parent=tmp_node , brach_length=int(son_len))
#                     phylo_dic[son] = son_node
#                 else:
#                     son_node = son
#                 tmp_node.s.append( son_node )
#                 son_node.p = tmp_node
#         else:
#             stack[-1] += nwk_s[idx] 
#         idx += 1
    
#     return phylo_dic

# file_path = 'd:/my_blog/github/Rosalind/test_data/NKEW_sample.txt' 
# queries = read_NKEW_file( file_path=file_path )
# for tmp_nwk,pair in queries:
#     tmp_graph = parse_nwk( tmp_nwk )
#     a,b = pair
#     print( tmp_graph[b].to_node(a) , end = ' ')


# use Phylo package to analysis newick format
import sys
import io
from Bio import Phylo 

queries = read_NKEW_file( file_path='d:/my_blog/github/Rosalind/test_data/NKEW_sample.txt' )

for i, pair in queries:
    a,b = pair
    tree = Phylo.read(io.StringIO(i),'newick') 
    sys.stdout.write('%s' % round(tree.distance(a,b)) + ' ') 
