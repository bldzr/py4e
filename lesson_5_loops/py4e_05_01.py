# Set initial variables to 0

total = 0
count = 0
average = 0

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

    #add number to total, increment count, and calculate average
    total = total + number
    count = count + 1
    average = total / count
    continue
    
#print results
# print ('All Done')
print(total, count, average)