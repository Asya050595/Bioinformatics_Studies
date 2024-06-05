from Bio import SeqIO
seq_list = [rec.id for rec in SeqIO.parse("input-seqnames.fasta", "fasta")]
print(*seq_list)
