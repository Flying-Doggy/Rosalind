#database
RNA_codon_map = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

DNA_codon_map = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


amino_mass_table = {"A":71.03711 , 'C':103.00919 , 'D':115.02694 , 'E':129.04259 , 'F':147.06841 , 'G':57.02146 , 'H':137.05891,
                  'I':113.08406 , 'K':128.09496 , 'L':113.08406 , 'M':131.04049 , 'N':114.04293 , 'P':97.05276 , 'Q':128.05858,
                  'R':156.10111 , 'S':87.03203 , 'T':101.04768 , 'V':99.06841 , 'W':186.07931 , 'Y':163.06333}


def read_fa_file( file_path:str , outfmt:str='dict'):
    if outfmt == 'dict':
        fa_dic = {}
        with open( file=file_path) as f:
            datas = f.readlines()
            for tmp_line in datas:
                if tmp_line.startswith('>'):
                    tmp_id = tmp_line[1:-1]
                    fa_dic[ tmp_id ] = ''
                else:
                    fa_dic[ tmp_id ] += tmp_line.strip('\n')
    elif outfmt == 'list':
        fa_dic = []
        with open( file=file_path) as f:
            datas = f.readlines()
            for tmp_line in datas:
                if tmp_line.startswith('>'):
                    fa_dic.append('')
                else:
                    fa_dic[-1]+= tmp_line.strip('\n')
    else:
        print( " outmt should be one of dict of list")
        return None
    return fa_dic

def DNA_rev_comp( DNA_seq:str ) ->str:
    base_map = {'A':'T' , 'T':'A' , 'C':'G' , 'G':'C' }
    rc_seq = ''
    for i in DNA_seq[::-1]:
        rc_seq += base_map[i]
    return rc_seq


def hamming( seq1:str , seq2:str ):
    # seq1 and seq2 should be equal length
    if len(seq1) != len(seq2):
        print( "%s and %s are not equal length, please check the input sequence"%( seq1 , seq2 ) )
        return 0
    else:
        mis_cnt = sum( [ seq1[i] != seq2[i] for i in range(len(seq1)) ] )
        return mis_cnt/len(seq1)
    

def edit_distance(seq1:str , seq2:str ): # Wagner-Fischer algorithm
    cur = list(range(len(seq1)+1))
    for j, s in enumerate(seq2):
        last, cur = cur, [j+1] 
        for i, t in enumerate(seq1):
            cur.append(last[i] if s==t else min([last[i+1], last[i], cur[-1]]) + 1)
    return cur[-1]

def edit_distance_fast( s: str, t: str) -> int:  
    # use one list to update distance
    f = list(range(len(t) + 1))
    for x in s:
        pre = f[0]
        f[0] += 1
        for j, y in enumerate(t):
            tmp = f[j + 1]
            f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
            pre = tmp
    return f[-1]




### TRIE
class trie_tree:
    def __init__(self , root:str ) -> None:
        self.root = trie_node( val=root , idx=1 )
        self.n = 1
        self.node_dic = { 1:self.root }
        pass

    def add_string( self, seq:str ) -> None:
        cur = self.root
        for i in seq:
            if cur.next.get(i):
                cur = cur.next.get(i)
            else:
                self.n += 1
                cur.next[i] = trie_node( val=i , idx=self.n )
                print( cur.idx,  self.n , i )
                cur = cur.next[i]
        pass

class trie_node:
    def __init__(self , val:str , idx:int ) -> None:
        self.val = val
        self.idx = idx
        self.next = { }
        pass

    def __repr__(self) -> str:
        return self.next
    
    def __str__(self) -> str:
        pass

###