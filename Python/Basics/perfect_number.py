st=int(input("Enter a starting point : "))
end=int(input("Enter a ending point : "))
for i in range(st,end+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i and i>1:
        print(i)