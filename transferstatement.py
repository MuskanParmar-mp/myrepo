'''n = int(input("Enter number"))
for i in range(1,n+1):
    if i==5:
        continue
    print(i)'''



''''n = int(input("Enter number: "))
i=1
while i<=n:
    if i==5:
        i=i+1
        continue
    print(i)
    i=i+1'''


'''n = int(input("enter any number:"))
i=1
while i<=n:
    if i==5:
        pass
    else:
        print(i)
        i=i+1'''


while True:
    print("1. Addition\n2. Sub\n 3. Multi\n 4." \
    "Division\n 5.Off")
    n=int(input("enter any of one option:"))
    x=(1,2,3,4,5)
    if n in x:
        pass
    else:
        print("Please enter valid option")




'''while True:
    print("1. Addition\n2. Sub\n 3. Multi\n 4." \
    "Division\n 5.Off")
    n=int(input("enter any of one option:"))
    x=(1,2,3,4,5)
    if n in x:
        y=(1,2,3,4)
    if n in y:  
        pass
    else:
        break'''





'''while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. OFF")
    n = int(input("Enter any one option: "))


    x = (1, 2, 3, 4, 5)
    if n in x:
        y = (1, 2, 3, 4)
        if n in y:
            if n == 1:
                tn = int(input("Please enter how many numbers you want to add: "))
                l = []
                for i in range(1, tn + 1):
                    value = int(input(f"Enter number {i}: "))
                    l.append(value)
                sum = 0
                for i in l:
                    sum = sum + i
                print(f"Sum of given values {l} is {sum}")
        elif n == 5:
            print("Turning OFF... Goodbye!")
            break
    else:
        print("Invalid option! Please try again.")'''


