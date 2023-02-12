# input 2 values that represent activity of 2 accounts
# if these value differ more than 3 times than one of the values is outlier (shlling profile)

print('Enter the first number:')
a = int(input())
print('Enter the second number:')
b = int(input())

if b > a*3:
    print("b is a shilling account")
    
elif a > b*3:
    print("a is a shilling account")
  
else:
  print("there is no shilling accounts")
