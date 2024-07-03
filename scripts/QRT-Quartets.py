# Quartets
# according to each line of partial character table, we can group all species into three parts( 0, 1 , x)
# if the numbers of part-0 and part-1 is greater than 2, the quartets can be operated

def read_QRT_file( file_path:str ) :
    with open( file= file_path) as f:
        datas = f.readlines()
        species = datas[0].strip().split()
        characters = [ list(i.strip('\n')) for i in datas[1:] ]
    return species,characters

def select_two( query:list ):   # select two ordered element from given list 
    res = []
    for i in range(len(query)):
        for j in range( i+1, len(query) ):
            res.append( (query[i], query[j]) )
    return res 

file_path = 'd:/my_blog/github/Rosalind/test_data/QRT_sample.txt'
species, characters = read_QRT_file( file_path= file_path )

group_dic = set()
for tmp_char in characters:
    present_list = []
    absent_list = []
    for idx,i in enumerate(tmp_char):
        if i == '1':
            present_list.append( idx )
        elif i == '0':
            absent_list.append( idx )
    
    if len(present_list) >=2 and len(absent_list) >= 2:
        a , b = select_two(present_list) , select_two(absent_list)
        for i in a:
            for j in b:
                group_dic.add( (i, j) if i[0] < j[0] else (j, i) ) # sort the pair to avoid repeat marking
    
for i,j in group_dic:
    print( '{' + ', '.join( set([ species[k] for k in i]) ) + '}' , 
          '{' + ', '.join( set([ species[k] for k in j]) ) + '}')
        