n = int(input("Enter the number of elements of fibonacci series:"))
fibo = [0,1]
if n>2:
    for i in range(2,n):
        nextelement = fibo[i-1] + fibo[i-2]
        fibo.append(nextelement)
print(fibo)
