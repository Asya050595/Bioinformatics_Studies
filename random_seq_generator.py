import sys
import random

my_list1 = ['A', 'T', 'G', 'C']
num = int(sys.argv[1])


my_list2 = [random.choice(my_list1) for x in range(num)]

pum = ''.join(my_list2)


newfile = open("random.fasta","w")
newfile.write(">random sequence of length " + sys.argv[1] + '\n' + pum)


