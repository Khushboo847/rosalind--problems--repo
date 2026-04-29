def find_motif_positions(sequence, motif):
    positions = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i : i + len(motif)] == motif:
            positions.append(i + 1)  
    return positions


def main():
    sequence = input("Enter the string: ").strip()
    motif = input("Enter the substring: ").strip()
    positions = find_motif_positions(sequence, motif)
    print(*positions)

if __name__ == "__main__":
    main()