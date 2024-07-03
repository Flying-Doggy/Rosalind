# Counting Unrooted Binary Trees
# when we add a new node to a (n)-node tree( n leaves and n-1 internal ), there can produce 2*n-1 (n+1)-nodes tree. [ for dinstict leaves ] 

# because all the labels are same, when n==2 or n==3, the b(n) = 1, the number of dinstinct edges change to (2*n-3)  
# b(n+1) = b(n)*(2*n-3) 

# https://rosalind.info/problems/cunr/explanation/ could be a reference. but haven't give a proof


MOD = 1_000_000
n = 888
prev_tree = 1
cur = 3
while cur < n:
    prev_tree *= (2*cur-3)
    prev_tree %= MOD
    cur += 1
print( prev_tree % MOD )

