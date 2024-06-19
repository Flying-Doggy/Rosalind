# Sorting by Reversals
# the script is almost same with REAR.
# but we need to take every reversal into memory

import collections

# start_seq = tuple( '1 2 3 4 5 6 7 8 9 10'.split() )
# end_seq =  tuple('1 8 9 3 2 7 6 5 4 10'.split() )

start_seq = tuple( '1 10 3 6 2 5 4 9 8 7'.split() )
end_seq =  tuple('10 6 1 4 7 9 5 8 3 2'.split() )

def reversal_search_bfs( start_seq:tuple, end_seq:tuple ):
    visited = collections.defaultdict( list )
    tmp_permu = collections.deque( [start_seq] )

    while tmp_permu:
        tmp_seq = tmp_permu.popleft()
        for i in range( len(tmp_seq) ):
            for j in range( i+1, len(tmp_seq)):
                new_per = tmp_seq[:i] + tmp_seq[i:j+1][::-1] + tmp_seq[j+1:]
                if visited.get( new_per ) != None:
                    continue
                visited[new_per] = visited[tmp_seq]+[ (i+1,j+1) ]

                if new_per == end_seq:
                    return visited[new_per]
                
                tmp_permu.append( new_per )

changes = reversal_search_bfs( start_seq=start_seq , end_seq=end_seq) 
print( len(changes) )
for i in changes:
    print( *i )