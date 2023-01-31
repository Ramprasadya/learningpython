a = input("Enter the Number : ")
print(f"multiplication table of {a} is :")

try:
    for i in range(1,11):
     print(f"{int(a)} X {i} is : {int(a)*i}")

except :
    print("Error")

print("The important line of code")