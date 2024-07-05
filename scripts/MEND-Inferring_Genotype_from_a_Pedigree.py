# Inferring Genotype from a Pedigree
# Tree Structure CNTQ,MEND,LREP

import math
import collections

possible_dict = { ('AA','AA'):(1,0,0) , ('AA','Aa'):(0.5,0.5,0) ,  ('AA','aa'):(0,1 ,0) , ('Aa', 'AA'):(0.5,0.5,0) , 
                  ('aa' ,'AA'):(0,1,0) , ('Aa' ,'Aa'):(0.25,0.5,0.25)  ,('Aa', 'aa'): (0,0.5,0.5) , ( 'aa' , 'Aa'): (0,0.5,0.5) ,
                  ('aa','aa'):(0,0,1)}

class Tree:
    def __init__(self , label:str = '' , parent =None , sons:list = [] , node_type:str = 'leaf' ) -> None:
        self.lab = label
        self.p = parent
        self.s = [ ]
        self.t = node_type
        self.poss = collections.defaultdict( float )
        pass
    
    def __repr__(self) -> str:
        if self.p == None:
            return 'cur_node:%s , parent:%s ,  sons:%s'%( self.lab , 'root' , ', '.join( str(i.lab) for i in self.s ) )
        elif self.t == 'leaf':
            return 'cur_node:%s , parent:%s ,  sons:%s'%( self.lab , 'root' , 'leaf' )
        else:
            return 'cur_node:%s , parent:%s ,  sons:%s'%( self.lab , self.p.lab , ', '.join( str(i.lab) for i in self.s ) )
    
    def get_possible( self ):
        if self.t == 'leaf':
            self.poss[ self.lab ] = 1
        else:
            a = self.s[0].get_possible()
            b = self.s[1].get_possible()
            for tmp_g1,tmp_p1 in a.items():
                for tmp_g2, tmp_p2 in b.items():
                    base_p = tmp_p1*tmp_p2
                    tmp_res = possible_dict[ tmp_g1 , tmp_g2 ]
                    self.poss[ 'AA' ] += base_p*tmp_res[0]
                    self.poss[ 'Aa' ] += base_p*tmp_res[1]
                    self.poss[ 'aa' ] += base_p*tmp_res[2]
        return self.poss


    

def parse_nwk( nwk_s:str ) -> dict:
    phylo_dic = collections.defaultdict( Tree )
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
            tmp_node = Tree( label=tmp_id, node_type='inter' , sons=[] )
            phylo_dic[tmp_id] = tmp_node

            tmp_sons = []
            while stack[-1] != '(':
                a = stack.pop()
                if a != '':
                    tmp_sons.append( a ) 
            stack.pop()
            stack.append( tmp_node )

            for son in tmp_sons:
                son_node = son
                if type(son) == str:
                    son_node = Tree( label=son , node_type='leaf' , parent=tmp_node)
                    phylo_dic[son] = son_node
                tmp_node.s.append( son_node )
                son_node.p = tmp_node
        else:
            stack[-1] += nwk_s[idx] 
        idx += 1
    
    return phylo_dic , tmp_node

nwk_tree = '(((((((((aa,Aa),(AA,aa)),((Aa,Aa),(AA,AA))),(((aa,AA),(aa,aa)),((Aa,aa),(AA,aa)))),((((aa,Aa),(Aa,AA)),((AA,aa),(AA,aa))),(((Aa,Aa),(aa,aa)),((Aa,Aa),(AA,Aa))))),(((((AA,AA),(Aa,AA)),((AA,AA),(AA,AA))),(((Aa,aa),(AA,aa)),((Aa,aa),(aa,aa)))),((((Aa,Aa),(Aa,AA)),((aa,aa),(Aa,AA))),(((Aa,Aa),(aa,AA)),((Aa,Aa),(AA,aa)))))),((((((AA,Aa),(aa,aa)),((AA,aa),(aa,AA))),(((Aa,aa),(AA,aa)),((aa,AA),(aa,aa)))),((((AA,aa),(aa,aa)),((aa,aa),(Aa,AA))),(((AA,aa),(AA,aa)),((aa,aa),(Aa,Aa))))),(((((AA,AA),(AA,aa)),((AA,aa),(aa,Aa))),(((aa,aa),(Aa,Aa)),((aa,AA),(AA,AA)))),((((Aa,AA),(Aa,Aa)),((aa,AA),(aa,aa))),(((Aa,aa),(Aa,AA)),((aa,AA),(aa,AA))))))),(((((((aa,aa),(AA,AA)),((aa,AA),(aa,Aa))),(((aa,aa),(Aa,Aa)),((Aa,Aa),(aa,aa)))),((((aa,Aa),(Aa,Aa)),((Aa,AA),(AA,AA))),(((aa,aa),(AA,AA)),((AA,aa),(aa,aa))))),(((((AA,AA),(aa,AA)),((aa,Aa),(AA,AA))),(((Aa,AA),(aa,aa)),((Aa,AA),(AA,aa)))),((((aa,aa),(Aa,aa)),((Aa,AA),(AA,Aa))),(((AA,AA),(aa,AA)),((Aa,Aa),(AA,Aa)))))),((((((aa,AA),(aa,AA)),((Aa,Aa),(Aa,Aa))),(((AA,AA),(AA,Aa)),((Aa,aa),(Aa,aa)))),((((aa,Aa),(Aa,aa)),((aa,Aa),(Aa,aa))),(((aa,Aa),(Aa,AA)),((aa,Aa),(AA,Aa))))),(((((aa,aa),(AA,Aa)),((Aa,AA),(AA,AA))),(((aa,AA),(Aa,AA)),((AA,AA),(aa,AA)))),((((Aa,Aa),(Aa,AA)),((Aa,Aa),(aa,AA))),(((aa,AA),(aa,AA)),((Aa,aa),(Aa,aa)))))))),((((((((Aa,aa),(AA,AA)),((aa,Aa),(Aa,Aa))),(((AA,Aa),(Aa,Aa)),((AA,AA),(Aa,Aa)))),((((Aa,aa),(Aa,Aa)),((aa,aa),(AA,AA))),(((AA,Aa),(aa,aa)),((Aa,aa),(AA,aa))))),(((((AA,AA),(aa,Aa)),((Aa,aa),(aa,AA))),(((Aa,aa),(aa,Aa)),((aa,AA),(AA,Aa)))),((((Aa,aa),(AA,AA)),((aa,AA),(AA,aa))),(((aa,AA),(AA,aa)),((Aa,AA),(Aa,Aa)))))),((((((AA,Aa),(AA,AA)),((AA,aa),(Aa,AA))),(((aa,aa),(AA,aa)),((aa,aa),(Aa,aa)))),((((AA,AA),(Aa,aa)),((Aa,Aa),(Aa,AA))),(((AA,Aa),(Aa,AA)),((aa,Aa),(Aa,aa))))),(((((aa,AA),(AA,AA)),((Aa,Aa),(AA,aa))),(((AA,aa),(Aa,AA)),((Aa,aa),(AA,aa)))),((((aa,AA),(Aa,AA)),((Aa,Aa),(aa,AA))),(((AA,AA),(aa,aa)),((AA,AA),(Aa,aa))))))),(((((((aa,aa),(aa,Aa)),((Aa,AA),(AA,Aa))),(((AA,AA),(AA,AA)),((AA,AA),(AA,aa)))),((((AA,AA),(Aa,Aa)),((AA,aa),(AA,AA))),(((AA,aa),(aa,AA)),((AA,AA),(AA,Aa))))),(((((AA,Aa),(aa,aa)),((AA,aa),(Aa,aa))),(((AA,Aa),(aa,Aa)),((AA,AA),(aa,AA)))),((((aa,Aa),(aa,Aa)),((Aa,AA),(aa,AA))),(((AA,Aa),(Aa,aa)),((aa,Aa),(AA,AA)))))),((((((aa,AA),(AA,Aa)),((Aa,AA),(aa,Aa))),(((aa,aa),(AA,AA)),((AA,aa),(aa,AA)))),((((aa,aa),(Aa,AA)),((Aa,AA),(AA,aa))),(((AA,Aa),(Aa,aa)),((AA,aa),(aa,Aa))))),(((((aa,AA),(aa,Aa)),((Aa,Aa),(aa,Aa))),(((AA,AA),(aa,AA)),((Aa,Aa),(aa,AA)))),((((aa,Aa),(aa,aa)),((Aa,AA),(AA,AA))),(((AA,Aa),(AA,Aa)),((aa,Aa),(AA,aa)))))))));'
node_dic,root = parse_nwk( nwk_s= nwk_tree )
root.get_possible()

print( root.poss['AA'] , root.poss['Aa'] , root.poss['aa']  )