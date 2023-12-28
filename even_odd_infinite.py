def check():
    data=int(input("Enter a number to check: "))
    if data % 2 == 0:
        print("Even Number")
    if data % 2 == 1:
        print("Odd Number")    

check()
n='y'
while n=='y' or n=='Y':
    n=input("Do you want to check again? ")
    if n=='y' or n=='Y':
        check()
    else:
        break    

