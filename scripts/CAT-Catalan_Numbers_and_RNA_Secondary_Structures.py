# noncrossing RNA match
# Catalan Numbers and RNA Secondary Structures
import collections

q_seq = 'UGGUUGCACCGGGUUUAAACGCGCAUGCGCAAUCGCCGCAUGUAGCUAUAUAUUAACCUGGAUAUCCAGCUUAUCGAUACACGUGACGAUGCAUGACGUACGUCAUUAAUCGCGACGGCUUUGCAUACGAGCGCGCGAAGCUUCAUAUGAUAUAAUUUAAAGAUAGCGCUCGGCCCCCGGGAUAUCUGCAGCUAGUCGGUGGGGGCCUACCCAUGAUCAUAGCCCUAUGCAUAUAACGUUAGAGCUAUCG'
# seq = 'AUAU'
MOD = 1000000

map_dic = {'A':'U' , 'U':'A' , 'C':'G' , 'G':'C'}

catalan_memory = { 'AU':1 , 'UA':1 , 'CG':1 , 'GC':1}

# finally I choose use substings as memory idx instead of index pair of strings, because different index pair may reflect to same sequence.
# Use substring can save memory and speed up 
def catalan_number( seq:str , cata_memo:dict ):
    if catalan_memory.get( seq ) != None:
        return catalan_memory.get(seq)
    else:
        if seq == '':
            return 1
        tmp_res = 0
        for i in range( 1, len(seq), 2):
            if seq[i] == map_dic[ seq[0] ]:
                # print( seq, i )
                tmp_res += catalan_number( seq[1:i]  ,cata_memo )*catalan_number( seq[i+1:]  ,cata_memo )
        cata_memo[ seq ] = tmp_res
    return tmp_res
    
print( catalan_number( seq=q_seq, cata_memo=catalan_memory) % MOD )




# def _get_catalan_numbers(s, nodes, catalan_memo):
#     n = int(nodes/2)
#     if n <= 1:
#         return 1
#     if catalan_memo.get((s, nodes),0):
#         return catalan_memo[(s, nodes)]
#     Cn = 0
#     for k in range(1, 2*n, 2):
#         a, u, c, g = s[1:k].count("A"), s[1:k].count("U"), s[1:k].count("C"), s[1:k].count("G")
#         if a==u and c==g and (s[0], s[k]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")]:
#             Cn += _get_catalan_numbers(s[1:k], k-1, catalan_memo) * _get_catalan_numbers(s[k+1:], 2*n-k-1, catalan_memo)
#     #  Memorize calculated Catalan Numbers values
#     catalan_memo[(s, nodes)] = Cn
#     return Cn

# print( _get_catalan_numbers(seq , len(seq) , catalan_memory) )



# def point_to_edge( point:int , edge:list ) -> str:
#     if point < edge[0]:
#         return 'left'
#     elif point > edge[1]:
#         return 'right'
#     else:
#         return False

# idx_dic = collections.defaultdict( set )
# for idx,val in enumerate( seq ):
#     idx_dic[val].add(idx)

# map_dic = {'A':'U' , 'U':'A' , 'C':'G' , 'G':'C'}

# def dfs( idx:int , graph:dict , visited:set,  edges:list ):
#     global cnt
#     if idx == len(seq):
#         cnt +=1
#     else:
#         if idx in visited:
#             dfs( idx+1 , graph=graph , visited=visited, edges=edges )
#         else:
#             visited.add( idx )
#             for paired_idx in graph[ map_dic[seq[idx]] ]:
#                 if paired_idx in visited or (paired_idx-idx)%2==0:
#                     continue
#                 else:
#                     if all( [ point_to_edge(idx,edge=edge) == point_to_edge(paired_idx,edge=edge) for edge in edges ] ):
#                         visited.add( paired_idx )
#                         dfs( idx+1 , graph=graph , visited=visited, edges=edges+ [(idx,paired_idx) ])
#                         visited.remove( paired_idx )
#             visited.remove(idx)

# dfs( 0 ,idx_dic , set() , list())

# print( cnt )