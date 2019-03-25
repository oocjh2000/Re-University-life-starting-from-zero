def main():
   total = int(input("구입금액을 입력하세요"))
   if total>=100000:
       total-=int(total*0.05)
       print("5%할인이 적용된 금액은"+str(total)+"원 입니다.")
   else:
       print(str(100000-total)+"원치를 더 구매하시면 5%할인을 받을 수 있습니다")
      
   
if __name__=="__main__":
    main()
    
