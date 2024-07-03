# Creating a Character Table from Genetic Strings

def read_CSTR_file( file_path:str ) -> list:
    with open( file= file_path ) as f:
        datas = f.readlines()
        outs = [ i.strip('\n') for i in datas ]
    return outs

file_path = 'd:/my_blog/github/Rosalind/test_data/CSTR_sample.txt'
seqs = read_CSTR_file( file_path= file_path )

for idx in range( len(seqs[0]) ):
    tmp_char = {}
    tmp_genotype = ''

    for i in seqs:
        if tmp_char.get( i[idx] ) == None:
            tmp_char[ i[idx] ] = str( 1- min(1,len(tmp_char)))
        tmp_genotype += tmp_char.get( i[idx] )        
    
    if tmp_genotype.count('0') <= 1 or tmp_genotype.count('1') <= 1:
        continue
    else:
        print( tmp_genotype )


# for i in range(len(seqs[0])):
#     nucleotides = [ seq[i] for seq in seqs]
#     non_trivial = len([ True for c in "ACTG" if nucleotides.count(c) > 1]) > 1
#     if non_trivial:
#         print ("".join([ ('1' if seq[i] == seqs[0][i] else '0') for seq in seqs]))
