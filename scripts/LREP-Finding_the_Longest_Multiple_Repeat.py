# Finding the Longest Multiple Repeat
# the Problem LREP have told the solution to find longest reapeat according to the given information 
# parse all edges and count the frequency of each substrings can get the result. 

import random

class tire_node:

    def __init__(self , parent = None , son = None , lab:str = '' ) -> None:
        self.p = parent
        self.s = [ ]
        if son:
            self.s.append( son )
        self.lab=  lab
        self.cnt = 0
        pass

    def sons_cnt( self ):
        if self.s:
            self.cnt = sum( [ i[0].sons_cnt() for i in self.s ] )
            return self.cnt
        else:
            return 1
    
    def get_longest( self , k , prev:str= ''):
        tmp_longest = set([''])    # store all the longest sequence
        for tmp_son,tmp_edge in self.s:
            if tmp_edge == '$' or tmp_son.cnt < k :   # to the end of substring or the number of substring is less than limit
                # record the current substring
                a = tmp_longest.pop()   # the poped element should be given back to the set
                if len(prev) > len( a ):
                    tmp_longest = set([prev])
                elif len(prev) == len( a ):
                    tmp_longest.add(prev)
                    tmp_longest.add(a)
                else:
                    tmp_longest.add(a)
                continue
            else:
                tmp_seq = tmp_son.get_longest( k , prev+tmp_edge  )
                b,a = tmp_seq.pop() , tmp_longest.pop()    # the poped element should be given back to the set
                if len( b ) > len(a):
                   tmp_longest = tmp_seq
                   tmp_longest.add( b)
                elif len(a) == len(b):
                   tmp_longest |= tmp_seq
                   tmp_longest.add( a )
                   tmp_longest.add(b)
                else:
                    tmp_longest.add(a)
        
        return tmp_longest
                

    def __repr__(self) -> str:   # output the cur tire_node information
        if self.p == None:
            return 'cur_node:%s , parent:%s , sons:%s'%( self.lab , 'root' , ', '.join( [ str( (i[0].lab , i[1]) ) for i in self.s ] ))
        return 'cur_node:%s , parent:%s , sons:%s'%( self.lab , self.p.lab , ', '.join( [ str( (i[0].lab , i[1]) ) for i in self.s ] ))

def read_LREP_file( file_path : str ):
    with open( file= file_path ) as f:
        datas = f.readlines()
        query_seq = datas[0].strip()
        lim_k = int( datas[1] )
        edges = [ i.split() for i in datas[2:] ]
    return query_seq, lim_k , edges

def parse_edges_to_substring( seq:str , edges:list ): # construct a suffix tree 
    node_dic = {}
    for tmp_p, tmp_s , s, e in edges:
        if node_dic.get(tmp_p) == None:
            node_dic[tmp_p] = tire_node( lab= tmp_p )
        if node_dic.get(tmp_s) == None:
            node_dic[tmp_s] = tire_node( parent=node_dic[tmp_p] ,lab= tmp_s )
        s,e = int(s) , int(e)
        edge = seq[ s-1:s-1+e ]
        node_dic[tmp_p].s.append( (node_dic[tmp_s], edge))
    return node_dic

file_path = 'd:/my_blog/github/Rosalind/test_data/LREP_sample.txt'
seq, k , edges = read_LREP_file( file_path=file_path)
node_dic = parse_edges_to_substring( seq= seq , edges=edges )
node_dic['node1'].sons_cnt()

print( node_dic['node1'].get_longest(k=k , prev=''   ) )


# BUT HOW TO GET A SUFFIX TREE?