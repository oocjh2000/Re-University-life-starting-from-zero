import pickle
import random
f=open('.\saving.bin','rb')
saving_accounts=pickle.load(f)
f=open('.\checking.bin','rb')
check_accounts=pickle.load(f)

sum_sav=0
sum_che=0
for i in range(5):
    sum_sav+=saving_accounts[i].deposit(random.randint(10000,1000000))
    sum_che+=check_accounts[i].deposit(random.randint(10000,1000000))

print("Saving Account Total:",sum_sav)
print("Checking Account Total:",sum_che)
accounts=check_accounts+saving_accounts
accounts=sorted(accounts,key=lambda accounts:accounts._BankAccount__balance)
print("최고액 보유자:",accounts[len(accounts)-1].name,"잔액 :",accounts[len(accounts)-1]._BankAccount__balance)
