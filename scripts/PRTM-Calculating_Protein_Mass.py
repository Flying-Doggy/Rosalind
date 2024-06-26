#Calculating Protein Mass
from sys import argv

def calculate_prot_mass( seq:str ) -> float :
    #amino mass data is from https://rosalind.info/glossary/monoisotopic-mass-table/
    mass_table = {"A":71.03711 , 'C':103.00919 , 'D':115.02694 , 'E':129.04259 , 'F':147.06841 , 'G':57.02146 , 'H':137.05891,
                  'I':113.08406 , 'K':128.09496 , 'L':113.08406 , 'M':131.04049 , 'N':114.04293 , 'P':97.05276 , 'Q':128.05858,
                  'R':156.10111 , 'S':87.03203 , 'T':101.04768 , 'V':99.06841 , 'W':186.07931 , 'Y':163.06333}

    mass_t = 0
    for i in seq:
        if mass_table.get(i) == None:   
            print( "%s is not a known amino acid" % (i) )
            return None
        else:
            mass_t +=  mass_table.get(i)
    
    return mass_t

# test_prot:YSTISTNTAMGNWQWTKLNAWDDYICYIASEAVWSAQEEDMMGLRFNGFSNCVWFYRFGLIEHDEDLWNAIQFKKLLEYEANQGFYTHTYWANWKFRLNNEWIGCEEPCVEVSPDTKGRPIQKSQSWPFSCERTCKKAYYEFCTWWRPGLRLFTFREHAERSHCFTHEFGQLLPIMWSMVTYTWIVEINGCCQSCWFNSCHDGMDKWTEPGAWWFHDGECTVEWSSGHAPCLKTYVFLQKHWKQAFWKWPCIRWCKTLCLPAFGCQGHSRSWMLAYNLTVQRPKDIRVHLHLCNCQVHYCVRFVENSLNNFAWQAVIHETHYWHVPKCSIDKNAEILDYVCGTHEKHAEKAPLMMWGSFSPQRWCVWRILSGQMVFVYQKGIQWPERHKKDWLHGYTHFMIIRPWDMMHRFCWKDFEDITNQGDCLESPGDYFLSPFLFGKCHYHYQKNEDSALVQYGPPEHPRGVKWDHSSYYYKGDPASKTKADYGMSWGESEFLKQQPLFTRGWMDRPLLTVWTDFDFHKNMERNVPCNIHHHSRPVNGWTKGWNEHKWINNKREDYEYNPIVLWTPMAMSKRPYHCMHLQVSVTIYVKMKANNNSCSYWKNRMMEDILYLLQYRCWVHSWPDSNFSTNTPMWEDRYGRSRVSHFSHYAYYIGQAMFHKSIRYGAYPHFFCADEWFHYNEHKVKVKTMEHDAGVAWDKKDEMPGKWVIEGGEACKHSVEDCFHTYPYRWYDNWRNLDSKRRPAPECVAYKVYIYHKASHKFYRTMQHFAIKYPEDSHSAFFAPRCCNSRDGRPANIIPEVKSYFPWPGQKVTQHSKGPHRIMLCLNKLFPVLCVCVGDPQHCWWFKFWHDRGDLRTVVDIWRTATVNEKWGYIVYHSLVTRTTGTSCFYHHIQTFDVFWFRKHSDTEVNYPHVQEWCCPQYEANMYDFSACITAFPQDASMASMPAKFRCQMLE
# result: 114851.01109000086
seq = argv[1]
print( calculate_prot_mass(seq=seq)) 