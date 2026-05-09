def reverse_translation():
    protein = input("Enter the protein sequence: ").strip()

    codon_count = {
        "F": 2, "L": 6, "S": 6, "Y": 2, "C": 2, "W": 1,
        "P": 4, "H": 2, "Q": 2, "R": 6, "I": 3, "M": 1,
        "T": 4, "N": 2, "K": 2, "V": 4, "A": 4, "D": 2,
        "E": 2, "G": 4,
    }

    ways = 1

    for aa in protein:
        ways = (ways * codon_count[aa]) 

    # Multiply by number of stop codons (UAA, UAG, UGA).
    ways = (ways * 3) 
    return ways


print(reverse_translation())
