f=open("파일입출력\TextFile1.txt",'r')
lines= f.readlines()
f.close()
spaces=0
tabs=0
for i in lines:
    spaces+=i.count(' ')
    tabs+=i.count('\t')

print(spaces)
print(tabs)