# The Wright-Fisher Model of Genetic Drift
from scipy.stats import binom

N, m ,g , k = map( int, '5 8 6 5'.split() )

cur_p = m/( 2*N )

def prob_next( p:float , g:int ,  k:int ):
    if g == 1:
        return 1-binom.cdf( k=k-1 , n=2*N , p=1-p )
    res = 0
    for i in range(2*N +1 ):
        res += binom.pmf( k=i , n=2*N , p=p )*prob_next( p= i/(2*N) , g=g-1 , k=k )
    return res

print( prob_next(p=cur_p, g=g, k=k ))
