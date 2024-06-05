import Bio
from Bio.Seq import Seq
text = input()
text = Seq(text)

print(text.reverse_complement())
