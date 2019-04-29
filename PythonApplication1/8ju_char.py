m=3
n=5
def main():
   # row=int(input())
   # col=int(input())
    list=[]
    list=init_list(list)
    display(list)
def init_list(list):
    list=[[row*n+col for row in range(m)]for col in range(n)]
    return list
def display(list):
    sum=0
    for i in range(m):
        for j in range(n):
            sum+=j
    print(sum)
    sum=0
    for i in range(m):
        for j in range(n):
            if j%2==0:
                sum+=j
    sum=0
    print(sum)
    for i in range(m):
        for j in range(n):
            if j%2!=0:
                sum+=j
    print(sum)

if __name__=='__main__':
    main()

