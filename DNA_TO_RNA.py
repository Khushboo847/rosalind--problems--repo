def DNA():

    seq = input(("Enter the DNA seq: "))
    RNA = seq.replace("T", "U")
    return RNA
    
print(DNA())