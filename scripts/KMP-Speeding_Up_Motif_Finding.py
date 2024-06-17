# Speeding Up Motif Finding
# KMP 
# create a suffix and prefix jump map

from self_database import read_fa_file

fa = read_fa_file( 'd:/my_blog/github/Rosalind/test_data/KMP_sample.txt' , outfmt='list')[0]

def KMP( seq:str ) -> list:
    jump_list = [ ]
    prefix = {}
    tmp_s = ''
    suffix = []
    for idx,val in enumerate(seq):
        # deal with suffix to find all jump-able suffix 
        new_suf = []
        tmp_jump = 0
        suffix.append( "" )
        for i in suffix:
            i = i +val
            if prefix.get( i )!= None:
                tmp_jump = max( tmp_jump, prefix.get( i )+1 )
                new_suf.append( i)
        jump_list.append( tmp_jump )
        suffix = new_suf
        
        # update prefix
        tmp_s += val
        prefix[ tmp_s ] = idx
        
    return jump_list



print( *KMP(fa))

