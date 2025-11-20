# Assignment operator
account_balance = 10000

# += simulating deposit
account_balance += 500
# same as account_balance = account_balance + 500
print(f"Account balance after deposit: ${account_balance}")

# -=
account_balance -= 6000
print(f"Account balance after withdraw: ${account_balance}")

# *=, let's say our friend won a conquest that will duplicated its account balance 
account_balance *= 2
print(f"Account balance after win: ${account_balance}")

account_balance /= 2
print(f"Account balance after apply /= : ${account_balance}")

account_balance %= 4 # 1125, no module so its 0
print(f"Account balance after apply %= : ${account_balance}")

# There are more assigment ops. please refer to the docs of a particular language for 
# further and deep study.

