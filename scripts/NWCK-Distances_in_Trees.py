# Distances in Trees
# the solution can be described that get the graph from newick tree, then bfs to find the minmum cost way
import collections

def read_NWCK_file( file_path:str ) -> list:
    res = []
    with open( file= file_path ) as f:
        datas = f.readlines()
        for i in range( 0, len(datas) ,3 ):
            nwk_tree = datas[i].strip()
            node_pair = datas[i+1].split()
            res.append( (nwk_tree, node_pair ) )
    return res

# get the non-oriented graph from newick tree
def parse_nwk( nwk_s:str ) ->dict:
    graph_dic = collections.defaultdict( list )
    internode_cnt = 0
    stack = [ '' ]
    idx = 0
    while idx < len(nwk_s):
        if nwk_s[idx] == ',' or nwk_s[idx] == ';' :
            stack.append( '' )
        elif nwk_s[idx]  == '(':
            stack[-1] += nwk_s[idx] 
            stack.append( '' )
        elif nwk_s[idx]  == ')':
            tmp_id = ''
            while nwk_s[idx+1] != ',' and nwk_s[idx+1] != ';' and nwk_s[idx+1] != ')':
                idx += 1
                tmp_id += nwk_s[idx]

            if tmp_id == '':
                tmp_id = internode_cnt
                internode_cnt += 1
            
            sons = []
            while stack[-1] != '(':
                a = stack.pop()
                if a != '':
                    sons.append( a ) 
            stack.pop()
            stack.append( tmp_id )

            for son in sons:
                graph_dic[ son ].append( tmp_id )
                graph_dic[ tmp_id ].append( son)
        else:
            stack[-1] += nwk_s[idx] 
        idx += 1
    
    return graph_dic

# use bfs to find the query start taxa to end taxa
def find_way( graph:dict , start , end ):
    path_dic = {}
    path_dic[start] = 0
    cur = collections.deque( [start] )
    while cur:
        tmp_node = cur.popleft()
        for next_node in graph[tmp_node]:
            if next_node == end:
                return path_dic[tmp_node]+1
            if path_dic.get(next_node) != None:
                continue
            else:
                path_dic[next_node] = path_dic[tmp_node]+1
                cur.append( next_node )


file_path = 'd:/my_blog/github/Rosalind/test_data/NWCK_sample.txt'
queries = read_NWCK_file(file_path=file_path)
for tmp_nwk,tmp_pair in queries:
    a,b = tmp_pair
    tmp_graph = parse_nwk( tmp_nwk )
    print( find_way( tmp_graph , a ,b) , end= ' ' )
