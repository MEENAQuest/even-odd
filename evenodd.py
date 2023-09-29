
def check(data):
    if data % 2 == 0:
        return True

data=int(input("Enter a number to check: "))
if check(data):
    print("Even")
else:
    print("Odd")    