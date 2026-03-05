def calc(year):
    age_calc = 2026 - year
    return age_calc
name = input("Enter your Name : ")
birthyear = int(input("Enter your birth year : "))
age = calc(birthyear)
print(f"Your name is {name} and your age is {age}")