# Set initial smallest and largest variables to None
smallest = None
largest = None

#ask user to enter a number. Give error if user enters non-integer value
while True: 
    number = input('Enter a number: ')
    
    if number == 'done':
        break
    #check if number is valid
    try:
        number = int(number)
    except:
        print('Invalid input')
        continue
        
    if smallest is None or number < smallest: 
            smallest = number

    if largest is None or number > largest:
            largest = number

#print results
# print ('All Done')
print('Maximum is', largest)
print('Minimum is', smallest)