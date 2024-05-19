#RNA Splicing
from self_database import read_fa_file,DNA_codon_map

file = "D:/my_blog/github/Rosalind/test_data/SPLC_sample"

fa_dic = read_fa_file(file_path= file)

max_len = 0
for i in fa_dic.keys():
    if len(fa_dic[i]) > max_len:
        total_DNA = fa_dic[i]
        max_id = i
        max_len = len(total_DNA)


for i in fa_dic.keys():   #cut the introns
    if i== max_id:
        continue
    else:
        #print( fa_dic[i] )
        total_DNA = total_DNA.replace( fa_dic[i] , "" )
    

print( ''.join([ DNA_codon_map[total_DNA[i:i+3]] for i in range(0,len(total_DNA),3) ] ) )

