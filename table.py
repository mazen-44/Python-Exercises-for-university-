try:
    n = int(input("Enter the size of multiplication table (default 10): "))
except ValueError:
    n = 10
print("    ", end="")
for i in range(1, n+1):
    print(f"{i:4}", end="")
print()
print("    " + "----"*n)
for i in range(1, n+1):
    print(f"{i:2} |", end="")
    for j in range(1, n+1):
        print(f"{i*j:4}", end="")
    print()