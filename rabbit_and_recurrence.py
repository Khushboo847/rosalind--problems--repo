def recurrence(n,m):
    if n <= 2:
        return 1
    return recurrence(n-1,m)+m*recurrence(n-2,m)

print(recurrence(5,3))