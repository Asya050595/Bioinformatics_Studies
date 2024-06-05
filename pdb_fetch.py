import sys
import wget
import requests


url = 'https://files.rcsb.org/download/{}.pdb'.format(sys.argv[1])

with open('{}.pdb'.format(sys.argv[1]), 'wb') as out_file:
    content = requests.get(url, stream=True).content
    out_file.write(content)

