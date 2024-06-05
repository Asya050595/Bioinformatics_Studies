import sys
import fileinput

def string(fname):
    with open(fname, "r", encoding="UTF-8") as F:
        try:
            lines = len(F.readlines())
            return lines
        except:
            return "can't"

for i in sys.argv[1:]:
     print(string(i))
