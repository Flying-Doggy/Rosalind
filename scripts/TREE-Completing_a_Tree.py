# The Tree of Life

# the first len encodes the number of nodes, the following lines encodes the edges
def read_input_file( file_name:str ):
    edges = []
    datas = open( file=file_name , mode="r" ).readlines()
    n = int( datas[0] )
    for i in datas[1:]:
        edges.append( map(int,i.split()) )
    return n,edges

n,edges = read_input_file( 'D:/my_blog/github/Rosalind/test_data/TREE_sample.txt' )
parents = [ i for i in range(n) ]

def find( x:int ) -> int :
    if x == parents[x]:
        return x
    else:
        parents[x] = find( parents[x] )
        return parents[x]

def union( edge:list ):
    x,y = edge
    parent_x , parent_y = find(x-1) , find(y-1)
    if parent_x == parent_y:
        return None
    else:
        if parent_x < parent_y:
            parents[parent_y] = parent_x
        else:
            parents[parent_x] = parent_y
        return None

for edge in edges:
    union( edge=edge) 

# print( parents )
# count the number of union_set
print( sum( [x==parents[x] for x in range(n)]) - 1 )