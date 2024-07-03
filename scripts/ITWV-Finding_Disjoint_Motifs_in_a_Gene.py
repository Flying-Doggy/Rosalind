# Finding Disjoint Motifs in a Gene
import functools

def read_ITWV_file( file_path:str ):
    with open( file= file_path ) as f:
        datas = f.readlines()
        tar = datas[0].strip('\n')
        candidates = [ i.strip() for i in datas[1:]]
    return tar,candidates

# 主要采用动态规划的方法，如果能够匹配，则逐级进行匹配，对于两条序列均可匹配的情况，有两种子情况（若允许重叠使用碱基则有三种情况）可以讨论
# 采用cache缓存结果
@functools.cache
def is_disjoint_motif( tar:str , s1:str , s2:str ) -> bool:
    if s1 == '' and s2 == '':
        return True
    elif s1 == '':
        if tar[0] == s2[0]:
            return is_disjoint_motif( tar=tar[1:] , s1=s1 , s2=s2[1:])
        else:
            return False
    elif s2 == '':
        if tar[0] == s1[0]:
            return is_disjoint_motif( tar=tar[1:] , s1=s1[1:] , s2=s2)
        else:
            return False
    
    if tar=='' or tar[0] != s1[0] and tar[0] != s2[0]:
        return False
    else:
        if tar[0] == s1[0] and tar[0] == s2[0] :
            return  is_disjoint_motif( tar=tar[1:] , s1=s1 , s2=s2[1:] ) or \
                is_disjoint_motif( tar=tar[1:] , s1=s1[1:] , s2=s2)
            # return is_disjoint_motif( tar=tar[1:] , s1=s1[1:] , s2=s2[1:] ) or \
            #     is_disjoint_motif( tar=tar[1:] , s1=s1 , s2=s2[1:] ) or \
            #     is_disjoint_motif( tar=tar[1:] , s1=s1[1:] , s2=s2)
        elif tar[0] == s1[0]:
            return is_disjoint_motif( tar=tar[1:] , s1=s1[1:] , s2=s2)
        else:
            return is_disjoint_motif( tar=tar[1:] , s1=s1 , s2=s2[1:] ) 



file_path = 'd:/my_blog/github/Rosalind/test_data/ITWV_sample.txt'

tar , candiates = read_ITWV_file( file_path=file_path )
n = len(candiates)
res = [ [0 for i in range(n)] for j in range(n) ]

for i in range(n):
    for j in range( i, n ):
        s1,s2 = candiates[i] , candiates[j]
        for idx,val in enumerate(tar):
            if val == s1[0] or val == s2[0]:
                if is_disjoint_motif( tar[idx:idx+len(s1)+len(s2)] , s1 , s2 ):
                    res[ i ][ j ] = res[ j ][ i ] = 1
                    break

for i in res:
    print( *i )
