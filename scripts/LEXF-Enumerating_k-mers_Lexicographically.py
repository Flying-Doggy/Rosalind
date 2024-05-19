#Enumerating k-mers Lexicographically

db = "A B C D E F G H".split()
n = 3
res = []

def dfs( times:int , prev:str ):
    if times == 0:    # Termination Conditions
        res.append( prev )
        return None
    times -= 1
    for new_s in db:
        dfs( times=times , prev=prev+new_s )
    return None

dfs( n , "")
res.sort()

for i in res:
    print( i )