import itertools

sequence = ' '
fasta = {}

with open('/home/asik/1.fasta') as file_one:
    for line in file_one:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                fasta[active_sequence_name] = []
            continue
        sequence = line
        fasta[active_sequence_name].append(sequence)

fasta = {k:v[0] for k,v in fasta.items()}
print(fasta)
