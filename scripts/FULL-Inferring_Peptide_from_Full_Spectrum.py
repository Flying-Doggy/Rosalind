# Inferring Peptide from Full Spectrum

from self_database import amino_mass_table
from sortedcontainers import SortedList

def read_FULL_file( file_path:str ):
    with open( file= file_path) as f:
        datas = f.readlines()
        total_L = float( datas[0] )
        subs = []
        for i in datas[1:]:
            subs.append( float(i) )
    return total_L, subs

mass_amino_dic = dict( [ [i[1],i[0]] for i in amino_mass_table.items()])

file_path = 'd:/my_blog/github/Rosalind/test_data/FULL_sample.txt'
total_len, specs = read_FULL_file( file_path= file_path )

visited = {}
for i in specs:
    visited[i] = 0

# 生成前后缀队列，每个序列都有可能作为前缀或后缀
specs.sort()
new_specs = []
for idx in range(len(specs)):
    new_specs.append( (specs[idx] , specs[len(specs)-1-idx]) )
specs = new_specs

res = ''
prev = specs[0][0]
visited[ specs[0][0] ] = visited[ specs[0][1] ] = 1
# 从小到大扫描前缀质量，判断其是否与已知氨基酸相符
for tmp,suf in specs[1:]:
    if visited[tmp]:
        continue 
    tmp_a = mass_amino_dic.get( round(tmp-prev,5) )
    if tmp_a:
        visited[tmp] = visited[suf] = 1 #表明这个序列对已经确定了位置了，后续再次遇到需要跳过
        res += tmp_a
        prev = tmp

print( res )


