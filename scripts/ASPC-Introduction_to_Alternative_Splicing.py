# Introduction to Alternative Splicing
# just sum all queried combination number

MOD = 1000000
# n , m = 1675,845
n,m = 6,3
tmp_num = res = 1

for i in range( n, m , -1):
    tmp_num *= i
    tmp_num //= (n-i+1)
    res += tmp_num%MOD

print( res%MOD )