from Bio import SeqIO

filename = input("Enter the file path: ")
max_gc = 0
max_id = ""
for record in SeqIO.parse(filename,"fasta"):
    seq = record.seq
    if len(seq) == 0:
        continue
    gc = ((seq.count("G") + seq.count("C")) / len(seq)) * 100
    if gc > max_gc:
        max_gc = gc
        max_id = record.id

print(max_id)
print(f"{max_gc:.6f}")













