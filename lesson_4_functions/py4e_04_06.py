
def computepay(hours, rate):
    if float(hours) > 40:
        extra_hours = float(hours) - 40
        extra_pay = extra_hours * float(rate) * 1.5
        gross_pay = 40 * float(rate) + extra_pay
    else:
        gross_pay = float(hours) * float(rate)
    return gross_pay

#enter hours worked
hours = input('Enter Hours: ')
#check for invalid input
try:
    hours = float(hours)
except:
    print('Error, please enter numeric input')
    quit()

#enter pay rate
rate = input('Enter Rate: ')

#check for invalid input
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

#calculate gross pay using above function
gross_pay = computepay(hours, rate)

#display gross pay
print('Pay', gross_pay)

