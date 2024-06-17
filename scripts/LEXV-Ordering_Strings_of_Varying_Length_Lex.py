# Ordering Strings of Varying Length Lexicographically
# use dfs to traverse all possible strings

alphabet = 'O U P Z K H G L T A D'.split()
k = 3
res = []

def dfs( loop:int , prev:str, res:list) -> None:
    if loop:
        for i in alphabet:
            new_s = prev+i 
            print( new_s )
            res.append( new_s)
            dfs( loop=loop-1 , prev=new_s , res=res)
    pass

dfs( loop=k , prev="" , res= res)