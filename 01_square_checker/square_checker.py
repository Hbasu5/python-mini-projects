#Squaring a number and check whether the squared value is odd or even
def new(d):
        q=d*d
        if(q%2==0):
            p='even'
        else:
            p='odd'
        return q,p
while(True):
    try:
         d=int(input("Enter a number ")) 
    except ValueError:
         print("Enter a number, previous input did not qualify.")
         continue
    output,output1 = new(d)
    print(f"The square of the number is {output}\nThe number is {output1}")
    c=input("Do you want to continue Y/N? ")
    if(c.lower()=='y'):
        continue
    elif(c.lower()=='n'):
        print("You chose to exit.")
        break
    else:
        print("Wrong Choice. Program exits")
        break