from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation={"+":add,
           "-":subtract,
           "*":multiply,
           "/":divide
           }

calculator="on"
prev=0
memory="no"
while calculator!="off":
    for symbol in operation:
        print(symbol)
    op=input("What operation you want to do? (Type Symbol): ")
    if memory=="yes":
        first=prev
        print("first value set to ",first)
        second = float(input("What is the second number?: "))
    else:
        first = float(input("What is the first number?: "))
        second = float(input("What is the second number?: "))
    ans=operation[op](first,second)
    prev=ans
    print(f"{first} {op} {second} = {ans}\n")
    choice=input("Would you like to continue? (Type 'yes' or 'no'): ")
    if choice=="no":
        calculator="off"
    elif choice=="yes":
        memory=input("\nWant to continue with previous answer? (Type 'yes' or 'no'): ")
        if memory=="yes":prev=ans
        else: prev=0