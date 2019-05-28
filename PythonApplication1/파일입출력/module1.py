f=open("TextFile1.txt",'r')
lines= f.readlines()
f.close()
f=open("TextFile1.txt",'w')
for i in range(len(lines)):
    line=str(i+1)+":"+lines[i]
    f.write(line)