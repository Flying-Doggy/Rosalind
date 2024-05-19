#Enumerating Gene Orders
def permutation( remains:list, cur:list , res:list ):
    if len(remains ) == 0:
        res.append(cur)
        print(*cur)
    for idx in range( len(remains) ):
        permutation( remains= remains[:idx]+remains[idx+1:] , cur = cur+[ remains[idx] ] , res=res  )
    return None

n = 7
new_remains = list( range(1,n+1) )
res = []

permutation( remains=new_remains , cur= [] , res=res )
print( len(res) )