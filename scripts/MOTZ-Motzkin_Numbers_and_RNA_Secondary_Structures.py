# Motzkin Numbers and RNA Secondary Structures
# not all paired bases is connected
# the script may be similar to CAT, mainly consider the equation ROSALIND gives: M_n=M_n-1+∑^n_k=2 (m_k-2)*(m_n-k)

motzkin_memo = { "AU":2 , "UA":2 , "CG":2 , "GC":2 }
map_dic = { 'A':'U' , "U":'A' , 'C':'G' , 'G':'C'}

def cal_num_motzkin( seq:str , mot_dic:dict ) ->int:
    if mot_dic.get( seq ) != None:
        return mot_dic.get( seq ) 
    else:
        if len(seq) <= 2:
            return motzkin_memo.get( seq , 1 )
        tmp_res = cal_num_motzkin( seq= seq[1:] , mot_dic=mot_dic)
        for i in range( 1, len(seq) ):
            if seq[i] == map_dic[seq[0]]:
                tmp_res += cal_num_motzkin( seq=seq[1:i] , mot_dic=mot_dic )*cal_num_motzkin( seq=seq[i+1:] , mot_dic=mot_dic )
        motzkin_memo[ seq ] = tmp_res
        return tmp_res
    
query = "CCACCGCCCUGAAGCCUUAUUACACUCCUGAUACGGAAUCAGCCUGUGUUGACGGUCGUUUAUAUCUGAGUCCCAUUCCGCGCUUAUGCGUAUAGCGAGUCUUUGAUUUUUGAGCGAGAUAAUUCAAACGUCCUGACAAAGUGCGUGGUAUAAAUGUUUGCACAGUUCUUCAUUGCGCCGCUGGAGGGGGAGAUUGCAAUUGCGCGAACCAGAUACCCAGUCAUUGCGUGCAUGAGCGGGUUCAGUCGUAAUAACGGACCUAAGAAGCGCGAAGAUCAGGUGCGGAUGGGCACAAUGAU"
MOD = 1000000
print( cal_num_motzkin(seq=query, mot_dic=motzkin_memo) % MOD)