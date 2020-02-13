# Rewrite your pay computation with time-and-a-half for overtime and create a function called compute pay which takes two parameters ( hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computePay(hours, rate):
    pay = 0
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        pay = (hours - 40) * (rate * 1.5) + (40 * rate)# extra hours * overtime rate plus regular pay
        return pay

# userHours = float(input("Enter hours: "))
# userRate = float(input("Enter the rate of pay: "))

print("Your Pay is: " + str(computePay(45, 10)))