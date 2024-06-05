import sys
import requests

url = 'https://www.uniprot.org/uniprot/{}.txt'.format(sys.argv[1])


with open('{}.txt'.format(sys.argv[1]), 'wb') as out_file:
    content = requests.get(url, stream=True).content
    out_file.write(content)


def get_pair(line):
    key, sep, value = line.strip().partition("   ")
    return str(key), value

with open('{}.txt'.format(sys.argv[1])) as fd:    
    d = dict(get_pair(line) for line in fd)

print(d.get("OS"))
