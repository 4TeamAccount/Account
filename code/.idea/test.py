change="[음식][식사] 1000 2021.01.25 14000"
money=+100
balance=change.split(' ')[-1]
new_balance= int(balance)- money
if new_balance < 0:
    print("잔고가 음수입니다...")
print(balance, new_balance)
change=change.replace(balance, str(new_balance))
print(change)