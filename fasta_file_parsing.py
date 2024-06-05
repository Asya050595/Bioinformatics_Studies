from Bio import SeqIO

fasta = "test1.fasta"

def fastaParser(infile):
    seqs = []
    headers = []
    with open(infile) as f:
        sequence = ""
        header = None
        for line in f:
            if line.startswith('>'):
                headers.append(line[1:-1])
                if header:
                    seqs.append([sequence])
                sequence = ""
                header = line[1:]
            else:
                sequence += line.rstrip()
        seqs.append([sequence])
    return headers, seqs

headers, seqs = fastaParser(fasta)

flat_seqs = [item for sublist in seqs for item in sublist]

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
        for seq in flat_seqs:
            print(key, countNucs(seq), file=f)
