# Synteny Blocks Have Orientations

n = 3
elements = set( range(1,n+1))
global cnt

cnt = 0
def dfs_orient_permutaion( gene_set:set , res:list ):
    if len(gene_set) == 0:
        print( *res )
        global cnt
        cnt += 1

    for i in gene_set:
        dfs_orient_permutaion( gene_set=gene_set-set([i]) , res=res +[i] )
        dfs_orient_permutaion( gene_set=gene_set-set([i]) , res=res +[-i] )

dfs_orient_permutaion( elements , res=[])
print( cnt )