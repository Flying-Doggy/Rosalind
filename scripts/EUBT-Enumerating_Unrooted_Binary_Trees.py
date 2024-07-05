# Enumerating Unrooted Binary Trees
import functools
from itertools import combinations

@functools.cache
def generate_trees( taxa ):  
    if len(taxa) == 2:
        # when the number of taxa is no more than 2, the structures of topology is unique
        return tuple( [ '(%s,%s)'%(taxa[0],taxa[1]) ])
    elif len(taxa) == 1:
        return tuple([ taxa[0] ] )
  
    trees = []  
    for i in range( 1, len(taxa)//2+1 ):  
        visited = set()
        # Recursively generate all left and right subtrees  
        for a in combinations( taxa,i ):
            b = [ j for j in taxa if j not in a ]   # get the complementary combination

            if len(a) == len(b):   # if a,b have the same length, there might be conflict sampling
               if a in visited:
                  continue
               visited.add(tuple(a) )
               visited.add(tuple(b) )

            a_subtrees = generate_trees( tuple(a) )  
            b_subtrees = generate_trees( tuple(b) )  # Skip the current taxon  
  
            # Combine left and right subtrees with the current taxon as the root  
            for a_tree in a_subtrees:  
                for b_tree in b_subtrees:  
                # Note: This is a simplified representation. In Newick, we'd need to format it properly.  
                    tree = '(%s,%s)'%(a_tree, b_tree)  
                    trees.append(tree)  
  
    return tuple(trees)  
  
taxa = 'Antilope_carnifex Capeila_rufodorsata Dendrobates_daurica Eschrichtius_carinatus Pterocles_sibilans Scaphiophryne_castus'.split() 
trees = generate_trees( tuple(taxa[1:]) )  
for i in trees:
   print( '(%s)%s;'%(i,taxa[0] ) )
