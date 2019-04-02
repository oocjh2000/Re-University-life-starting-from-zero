def bokun(n):
    sum=0
    if n%17>8:
        n+=17
        n=n*(n//3)
    else:
     n=n*(n//3)
    for i in range(1,n):
        if i%3==0:
            continue
        sum+=i
    return sum

n=int(input())
print(bokun(n))
