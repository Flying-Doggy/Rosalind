# Edit Distance Alignment
# this solution is similar to EDIT. the only difference is change iteral numbers into paired strings

from self_database import read_fa_file
file_path = 'd:/my_blog/github/Rosalind/test_data/EDTA_sample.txt'

seq1,seq2 = read_fa_file( file_path= file_path , outfmt='list' )

def edit_align( seq1:str , seq2:str ):
    cur = [ ('','',0) ]
    for i in seq1:
        cur.append( (cur[-1][0]+ i , cur[-1][1] + '-', cur[-1][2]+1 ) )
    
    for j in seq2:
        last, cur = cur , [ ]
        for idx in range( len(last) ):
            if idx == 0:
                cur.append( ( last[idx][0]+'-' , last[idx][1]+ j , last[idx][2]+1  ))
            else:
                # find current least edit distance alignment for three choices
                gap1_1_align, gap1_2_align , cnt_1 = cur[idx-1][0]+seq1[idx-1], cur[idx-1][1]+'-' , cur[idx-1][2]+1
                gap2_1_align, gap2_2_align , cnt_2 = last[idx][0]+ '-', last[idx][1] + j , last[idx][2]+1
                no_1_align, no_2_align , cnt_3 = last[idx-1][0]+seq1[idx-1] , last[idx-1][1]+j , last[idx-1][2]+(seq1[idx-1]!=j)
                if cnt_3 < cnt_2:
                    if cnt_3 < cnt_1:
                        cur.append( ( no_1_align, no_2_align , cnt_3  ) ) 
                    else:
                        cur.append( ( gap1_1_align, gap1_2_align , cnt_1))
                else:
                    if cnt_2 < cnt_1:
                        cur.append( ( gap2_1_align, gap2_2_align , cnt_2 ))
                    else:
                        cur.append( ( gap1_1_align, gap1_2_align , cnt_1) )
    return cur[-1]


res = edit_align(seq1=seq1 , seq2=seq2 )
print( '%d\n%s\n%s'%(res[2],res[0],res[1]) )