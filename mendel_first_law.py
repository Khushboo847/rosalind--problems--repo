#Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

def probability(k,m,n):
    N = k+m+n

    P = (k*(k-1) + 2*k*m + 2*k*n + 0.75*m*(m-1) +m*n)/(N*(N-1))
    return P

print(f"{probability(2,2,2):.5f}")
