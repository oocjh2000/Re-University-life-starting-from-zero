price=int(input("물건값을 입력하세요"))
thou=int(input("1000won : "))
five=int(input("500won : "))
one=int(input("100won : "))
total=(thou*1000)+(five*500)+(one*100)
res=total-price
thou=res//1000
res=res%1000

five=res//500
res=res%500

one=res//100
res=res%100

ten=res//10
res=res%10

print("1000 is "+str(thou)+" 500 is :"+str(five)+" 100 is :"+str(one)+" 10 is :"+str(ten))