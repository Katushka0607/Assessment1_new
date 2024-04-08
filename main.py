"""
OrderOfNumbers
"""
# Provide your solution here

n1 = int(input("Enter number 1 (n1): "))
n2 = int(input("Enter number 2 (n2): "))
if n1 <= 0 or n2 <=0:
    print("n1 and n2 need to be > 0")
elif n2 < n1:
    print("n2 needs to be > n1")
else:
    while n1 <= n2:
        print(str(n1) + " ", end="")
        n1 += 1
print(" \n")

"""
SumUp
"""
# Provide your solution here

while True:
    n1 = int(input("Enter number 1 (to quit enter -1): "))
    n2 = int(input("Enter number 2 (to quit enter -1): "))
    n3 = int(input("Enter number 3 (to quit enter -1): "))
    if n1 == -1 or n2 == -1 or n3 == -1:
        break
    if n3 > n2 > n1:
        print("numbers are ascending")
    elif n1 > n2 > n3:
        print("numbers are descending")
    else:
        if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
            print("no specific order, but all even")
        elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
            print("no specific order, but all odd")
        else:
            print("no specific order")
print("Thanks and bye!")
