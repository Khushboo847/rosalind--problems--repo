def DNA(seq):
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")

    return A , C , G ,T

a, c, g, t = DNA("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
print(a, c, g, t)
