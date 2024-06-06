
hours_worked = input('Enter Hours: ')
pay_rate = input('Enter Rate: ')

if float(hours_worked) > 40:
    extra_hours = float(hours_worked) - 40
    extra_pay = extra_hours * float(pay_rate) * 1.5
    gross_pay = 40 * float(pay_rate) + extra_pay
else:
    gross_pay = float(hours_worked) * float(pay_rate)

print('Pay:', gross_pay)

