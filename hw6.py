def calc(bill):
    total = 0
    if bill <= 150 : 
        total = bill * 1.50
    elif bill > 150 and bill <= 300:
        total = (150 * 1.50)+ ((bill - 150) * 2.20)
    else :
        total = (150 * 1.50)+ (150 * 2.20) + ((bill - 300) * 3.80)
    return total
while True:
    try : 
        given_bill = float(input("Enter your consumption (KWh) : "))
        if given_bill < 0 : 
            print("The Bill must be positive")
            continue
        break
    except ValueError : 
        print("The Bill must be numerical")
final_bill = calc(given_bill)
print(f"Your bill in TL is : {final_bill:.2f}")