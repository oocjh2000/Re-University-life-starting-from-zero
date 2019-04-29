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
    for i in range(n):
        for j in range(m):
            sum+=list[i][j]
    print(sum)
    sum=0
    for i in range(n):
        for j in range(m):
            if list[i][j]%2==0:
                sum+=list[i][j]
    print(sum)
    sum=0
    for i in range(n):
        for j in range(m):
            if list[i][j]%2==1:
                sum+=list[i][j]
    print(sum)

if __name__=='__main__':
    main()

