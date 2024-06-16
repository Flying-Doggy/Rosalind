# A^k_n simple permutation

MOD = 1000000
# n , k = 21 , 7
n,k = 84, 9

res = 1
for i in range( k ):
    res *= (n-i)

print(res%MOD)