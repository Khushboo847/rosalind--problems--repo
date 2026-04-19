def hamming_distance():
    seq_1 = input("Enter the sequence 1: ")
    seq_2 = input("Emter the sequnce 2: ")

    mutation = 0
    for i in range(len(seq_1)-1):
        if seq_1[i] != seq_2[i]:
            mutation += 1
    return mutation

print(hamming_distance())
        