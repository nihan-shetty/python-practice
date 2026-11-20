n=int(input("Enter a number : "))
s = True
num =n+1
while s:
    for i in range(1,n+1):
        if num%i!=0:
            num+=1
            break
    else:
        break
print(num)

