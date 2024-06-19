# Wobble Bonding and RNA Secondary Structures
# Wobble bonding: U can match to G
# like Motzkin numbers, we should take this problem into two parts, first base get paired and not paired

wobble_memo = {}

map_dic = set([ 'AU' ,'UA' ,'UG' ,'GU' , 'CG','GC'])

def get_wobble_number( seq:str , wobble_memo:dict ) -> int:
    if wobble_memo.get( seq ):
        return wobble_memo.get(seq)
    if len(seq) <5:
        return 1
    elif len(seq) == 5:
        wobble_memo[seq] = 1 + ( seq[0]+seq[-1]  in map_dic )
        return wobble_memo[seq]
    else:
        tmp_res = 0
        tmp_res += get_wobble_number( seq[1:], wobble_memo= wobble_memo )
        for i in range( 4,len(seq) ):
            if seq[0]+seq[i]  in map_dic:
                tmp_res += get_wobble_number( seq=seq[1:i] , wobble_memo= wobble_memo )*get_wobble_number( seq=seq[i+1:] , wobble_memo=wobble_memo)
        wobble_memo[seq] = tmp_res
        return tmp_res
    
query_seq = 'GGUCCGGGCAUAUGCAGCGGUACGCAACGACGGUCACGAUUCCUGUUCGGUCAGCCUUCCACUCAGCUAUAACGCAUCGCAGCAUCCACUGCAAAUACCAGACUUUACUAAAUAGUUGUGCUUUAGAAACACAAGCUCGCCAUAGAUGCCUAUAGGCCUCACCGUGGCAACUCA'
# seq = 'CGAUGCUAG'
print( get_wobble_number(seq=query_seq, wobble_memo= wobble_memo) ) 