sum = 0
mul = 1
while True:
    num = int(input("Please enter a number: "))
    if(num != -1):
        sum = sum + (num * mul)
        mul = mul + 1
    else:
        sum = sum + (num * mul)
        break
print (sum)