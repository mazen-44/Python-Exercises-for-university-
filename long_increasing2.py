count = 0
max_count =0 
prev = None
while True:
    num = int(input("Enter the number (-1 to stop) : "))
    if num == -1:
        break
    if prev is not None and num > prev:
        count +=1
    else:
        count = 0
    if count > max_count:
        max_count = count
    prev = num
print(f"The maximum increasing is : {max_count}")