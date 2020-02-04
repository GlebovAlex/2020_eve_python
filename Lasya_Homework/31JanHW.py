'''
Rewrite your pay computation with time-and-a-half for overtime and
 create a function called compute pay which takes two parameters ( hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

def computepay (hours, rate):

  if hours > 40:
    pay = hours * rate + (hours - 40) * rate/2
  else:
    pay = hours * rate
  return pay

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
print(computepay(hours, rate))
