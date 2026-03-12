count = 0
max_count=0
numbers = []
while True:
    num = int(input("Enter the number (-1 to stop) : "))
    if num == -1 :
        break
    numbers.append(num)
for i in range(1, len(numbers)) :
    if numbers[i] > numbers[i-1]:
        count += 1
        if count > max_count:
            max_count = count
    else :
        count =0
print(f"The maximum increasing is : {max_count} ")