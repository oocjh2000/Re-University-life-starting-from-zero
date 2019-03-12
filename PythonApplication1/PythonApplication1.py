principal = int(input("원금입력 : "))
interest = float(input("이자율 입력(%) : "))
interest=interest*0.01
year= int(input("상환기간 입력 : "))
res=principal
for year in range(24):
    res+= res * interest

print("---------------------------------------------")
print("원금 : "+ str(principal))
print("이자율 : "+str(interest*100))
print("상환기간 : "+str(year+1))
print("상환해야할금액 : "+str(res))
//

  