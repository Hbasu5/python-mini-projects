#LIST OPERATIONS
print("INSTRUCTION: Upon entering 0, the input process will stop and the program continues its further operations:")
number=[]
while True:
    try:
        n=int(input("Enter the number which you want to enter: "))
    except ValueError:
        print("Enter a number, previous input did not qualify.")
        continue
    if(n==0):
        z=input("You entered 0, do you really want to stop inputting numbers? Y: ")
        if(z.lower()=='y'):
            break
        elif(z.lower()=='n'):
            continue
        else:
            print("Wrong choice entered, we continue")
            continue
    else:
        number.append(n)
print("Numbers entered: ")
for s in number:
    print(s)
if number:
    print("Sum:", sum(number))
    print("Max:", max(number))
    print("Min:", min(number))
else:
    print("No numbers were entered.")