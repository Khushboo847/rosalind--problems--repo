def reverse_complement():

    DNA = input("Enter the DNA seq: ")
    reverse = DNA[::-1]
    complement = {
        "A" : "T",
        "T" : "A",  
        "C" : "G",
        "G" : "C"
    }
    result = ""
    for i in reverse:
        result += complement[i]

    return result

print(reverse_complement())