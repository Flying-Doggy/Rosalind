# Inferring Protein from Spectrum

from self_database import amino_mass_table
import bisect
from itertools import pairwise
from sortedcontainers import SortedList


def read_SPEC_file( file_path:str ) -> list:
    res = []
    with open( file= file_path ) as f:
        datas = f.readlines()
        for i in datas:
            res.append( float(i) )
    return res

def infer_pep( spec_list:list , mass_table:dict ) -> str:
    mass_table = SortedList( mass_table.items() , key= lambda x:x[1] )
    mass_table.add(['PEP',100000])
    mass_table.add(['PEP',0])
    res = ''
    for tmp_m in spec_list:
        tmp_idx = mass_table.bisect_left(  ('',tmp_m) )
        res += sorted( mass_table[tmp_idx-1:tmp_idx+2] , key= lambda x:abs(x[1]-tmp_m) )[0][0]

    return res

file_path = r'D:\my_blog\github\Rosalind\test_data\SPEC_sample.txt '
specs = read_SPEC_file( file_path= file_path )
specs = [ y-x for x,y in pairwise(specs)]
print( infer_pep(spec_list=specs , mass_table=amino_mass_table) )
