numbers = []
while True:
    try:
        n = int(input("Enter a value (To stop enter -1) : "))
    except ValueError:
        print("Please Enter a number : ")
        continue
    if n == -1:
        break
    numbers.append(n)
if len(numbers) == 0:
    print("No numbers has been entered")
else:
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd +=1
    count = len(numbers)
    maximum= max(numbers)
    minimum = min(numbers)
    total = sum(numbers)
    avg = total / count
    print(f"Count: {count}")
    print(f"Max: {maximum}")
    print(f"Min: {minimum}")
    print(f"Sum: {total}")
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")
    print(f"Average: {avg:.2f}")