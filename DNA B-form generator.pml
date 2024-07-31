cmd.do("reinitialize")

cmd.fetch('1D65')
cmd.remove('resn hoh')
cmd.do('''
create pair, resi 22+3
create nextpair, resi 21+4
create 1, pair 
pair_fit pair, nextpair
''') # create 1 - чтобы не жаловался, что не совпадает число атомов при стыковке
transformation = cmd.get_object_matrix("pair") # will return a list of floats with that matrix for a named object.
for i in range(2,50):
    cmd.create(str(i), str(i-1)) # creates a new molecule object from a selection.
    cmd.transform_selection(str(i), transformation, homogenous=0) # applies a transformation matrix to a selection
cmd.delete('1D65')
cmd.show('sticks')
