def calc(height , weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi
given_height = float(input("Enter your height in CM : "))
given_weight = float(input("Enter your weight in KG : "))
thebmi = calc(given_height,given_weight)
print(f"Your BMI is {thebmi:.2f}")