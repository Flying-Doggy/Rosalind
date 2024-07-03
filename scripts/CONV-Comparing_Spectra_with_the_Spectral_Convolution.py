# Comparing Spectra with the Spectral Convolution
import collections
def read_CONV_file( file_path:str ) -> list:
    with open(file= file_path ) as f:
        datas = f.readlines()
        res = [ list(map(float, i.split())) for i in datas ]
    return res 

cnt_dic = collections.defaultdict(int)
a,b = read_CONV_file( file_path= 'd:/my_blog/github/Rosalind/test_data/CONV_sample.txt' )

# calculate S_1 - S_2
for i in a:
    for j in b:
        cnt_dic[ round(i-j,5) ] += 1

# find the most fruquent key in  Minkowski difference 
tmp_max = 0
for tmp_dif,tmp_cnt in cnt_dic.items():
    if tmp_cnt > tmp_max:
        tmp_max = tmp_cnt
        res = tmp_dif

print( tmp_max , '\n', res )
