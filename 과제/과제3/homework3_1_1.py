#!/usr/bin/python
# -*- coding: <utf-8> -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
import bank
import random
import pickle
saving_accounts=[]
check_accounts=[]
for i in range(5):
    var=bank.SavingsAccount('sav'+str(i),i,random.randint(10000,100000),random.randint(1,10)*0.01)
    saving_accounts.append(var)
    var=bank.CheckingAccount('che'+str(i),i,random.randint(10000,100000))
    check_accounts.append(var)
f=open('.\saving.bin','wb')
pickle.dump(saving_accounts,f)
f=open('.\checking.bin','wb')
pickle.dump(check_accounts,f)
print('계좌정보가 저장되었습니다 homework3_1_2를 실행해주세요')