
def add(a, b):
    answer = a+b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer))

def sub(a,b):
    answer  = a-b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer))

def mul(a,b):
    answer = a*b
    print(str(a) + ' * ' + str(b) + ' = ' + str(answer))

def div(a,b):
    answer = a//b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer))


print("A. Addition")
print("B. Subtraction")
print("C. Division")
print("D. Multiplication")

choice = input("Enter your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    add(a,b)
elif choice == "b" or choice == "B":
    print("Subtration")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    sub(a,b)
elif choice=="c" or choice=="C":
    print("Division")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    while b == 0:
        print("Second number cannot be zero.Please enter a valid number.")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
    else:
        div(a,b)
elif choice == "d" or choice == "D":
    print("Multiplication")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    mul(a,b)
elif choice == "e" or choice == "E":
    print("PROCESS ENDED!!")
    quit()

