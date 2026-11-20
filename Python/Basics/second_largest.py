a=int(input("Enter a number :"))
largest=-1
sLargest=-1
if a<0:
    a=-(a)
while a>0:
    digit=a%10
    if digit>largest:
        sLargest=largest
        largest=digit
    elif digit>sLargest and digit<largest:
        sLargest=digit
    a//=10
if sLargest==-1:
    print("No second largest distinct")
else:
    print("Second Largest is : ",sLargest)