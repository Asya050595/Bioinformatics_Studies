def fastaParser(infile):
    sequences = []
    headers = []
    with open(infile) as f:
        sequence = ""
        header = None
        for line in f:
            if line.startswith('>'):
                headers.append(line[1:-1])
                if header:
                    sequences.append([sequence])
                sequence = ""
                header = line[1:]
            else:
                sequence += line.rstrip()
        sequences.append([sequence])
    return sequences

input_file = '/home/asik/HA_H1N1_2020.fasta'
sequences = fastaParser(input_file)
chain = sequences[0][0]

my_list = []
my_list.append(chain[:15])
k = 4
m = 19
for i in chain:
    my_list.append(chain[k:m])
    k += 4
    m += 4
    for x in my_list:
        if (len(x) == 15):
            continue
        else:
            my_list.remove(x)

output_file = '/home/asik/output_file.txt' 

with open(output_file, 'w') as out:
    out.write('\n'.join(my_list))
