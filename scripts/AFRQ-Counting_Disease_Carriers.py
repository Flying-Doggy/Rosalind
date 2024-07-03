# Counting Disease Carriers 

import math

def homo_re_to_carriers( prob:float ) -> float:
    dom_prob = 1- math.sqrt( prob )
    return 1-dom_prob**2

queries = map( float , '0.901818865512 0.73935054415 0.167852207844 0.962873995954 0.459077285624 0.047541950782 0.395043218685 0.80111203086 0.561915298461 0.765481086641 0.970929781001 0.960698372566 0.420442416024 0.322957656314 0.253574420536 0.80027818452 0.304593049272 0.515771697893 0.820678849495'.split())

for i in queries:
    print( round(homo_re_to_carriers(i) , 3 ) , end= ' ')