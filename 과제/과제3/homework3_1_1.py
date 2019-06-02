import bank
import random
import pickle
saving_accounts=[]
check_accounts=[]
for i in range(5):
    var=bank.SavingsAccount('sav'+str(i),i,(i+1)+100000,i+1*6.3)
    saving_accounts.append(var)
    var=bank.CheckingAccount('che'+str(i),i+5,(i+1)*10000)
    check_accounts.append(var)
f=open('과제3\saving.bin','wb')
pickle.dump(saving_accounts,f)
f=open('과제3\checking.bin','wb')
pickle.dump(check_accounts,f)