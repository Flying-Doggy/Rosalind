# Counting Phylogenetic Ancestors
# in the description of rooted trees.
# a binary tree can include nodes having degree 2, an unrooted binary tree is defined more specifically: all internal nodes have degree 3.
# In turn, a rooted binary tree is such that only the root has degree 2 (all other internal nodes have degree 3).

# And all leaf node (n) has degree 1 to a inertnal node. we set the number of internal nodes as 'x'. we can establish the following equation:
# 3*x = n + 2*(x-1)     /// total_degree_of_internodes = internode_to_leaf_degree + internode_to_indernode_degree 
# x = n-2

n = 1904

print( n - 2)