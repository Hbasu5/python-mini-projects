#DICTIONARY OPERATIONS
user={
}
user["Name"]=input("Enter your name: ")
user["Age"]=int(input("Enter your age: "))
for key, value in user.items():
    print(key,":",value)
try:
    ch=int(input("Which key do you want to change?\nEnter 1 for Name, Enter 2 for Age and Enter 3 for both: "))
except ValueError:
    print("Input did not qualify")
    ch=None
if(ch==1) or ch==3:
    user["Name"]=input("Enter the new Name: ")
if(ch==2 or ch==3):
    user["Age"]=int(input("Enter the new age: "))
else:
    print("Dictionary remains unchanged")
for key, value in user.items():
    print(key,":",value)