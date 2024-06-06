#enter hours worked
hours_worked = input('Enter Hours: ')
#check for invalid input
try:
    hours_worked = float(hours_worked)
except:
    print('Error, please enter numeric input')
    quit()

#enter pay rate
pay_rate = input('Enter Rate: ')

#check for invalid input
try:
    pay_rate = float(pay_rate)
except:
    print('Error, please enter numeric input')
    quit()

#calculate gross pay
if float(hours_worked) > 40:
    extra_hours = float(hours_worked) - 40
    extra_pay = extra_hours * float(pay_rate) * 1.5
    gross_pay = 40 * float(pay_rate) + extra_pay
else:
    gross_pay = float(hours_worked) * float(pay_rate)

#display gross pay
print('Pay:', gross_pay)

