num = int(input("Enter a number : "))
num=abs(num)
for i in range(10):
    temp = num
    count=0
    while temp>0:
        digit = temp%10
        temp//=10
        if digit==i:
            count+=1
    if count>0:
        print(i,"occurs",count,"times")
if num==0:
    print(num,"occurs",1,"times")