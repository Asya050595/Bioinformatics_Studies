from Bio import SeqIO

fasta = "test1.fasta"

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
    return headers, sequences

headers, sequences = fastaParser(fasta)

flat_sequences = [item for sublist in sequences for item in sublist]

def countNucs(instring):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    g = instring.upper().count('G')
    c = instring.upper().count('C')
    a = instring.upper().count('A')
    t = instring.upper().count('T')
    all = g + c + a + t
    return '{A} {C} {G} {T} {all}'.format(A = a, C = c, G = g, T = t, all = all)


with open('fasta_parse.txt', 'w') as f:
    print("Name   a   c   g   t   All", file=f)
    seq_dict = {rec.id : rec.seq for rec in SeqIO.parse("test1.fasta", "fasta")}
    for key, value in seq_dict.items():
        for seq in flat_sequences:
            print(key, countNucs(seq), file=f)
