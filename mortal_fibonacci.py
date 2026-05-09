def mortal_fibonacci(n,m):
    rabbits = [0]*m
    rabbits[0] =1

    for month in range(1,n):
        births = sum(rabbits[1:])
        rabbits = [births] + rabbits[:-1]
    return sum(rabbits)

print(mortal_fibonacci(6,3))
