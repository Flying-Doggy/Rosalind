# Introduction to Pattern Matching
# create a trie to encode all strings

class trie_tree:
    def __init__(self , root:str ) -> None:
        self.root = trie_node( val=root , idx=1 )
        self.n = 1
        self.node_dic = { 1:self.root }
        pass

    def add_string( self, seq:str ) -> None:
        cur = self.root
        for i in seq:
            if cur.next.get(i):
                cur = cur.next.get(i)
            else:
                self.n += 1
                cur.next[i] = trie_node( val=i , idx=self.n )
                print( cur.idx,  self.n , i )
                cur = cur.next[i]
        pass

class trie_node:
    def __init__(self , val:str , idx:int ) -> None:
        self.val = val
        self.idx = idx
        self.next = { }
        pass

    def __repr__(self) -> str:
        return self.next
    
    def __str__(self) -> str:
        pass
    
def read_TRIE_file( file_path:str ) -> list:
    res = []
    with open( file= file_path) as f:
        datas = f.readlines()
        for i in datas:
            res.append( i.strip() )
    return res

file_path = 'd:/my_blog/github/Rosalind/test_data/TRIE_sample.txt'
seqs = read_TRIE_file( file_path=file_path )
tmp_tree = trie_tree( root="" )
for i in seqs:
    tmp_tree.add_string(i)