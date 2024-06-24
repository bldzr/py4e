# create empty list and set error_count to 0
numlist = list()
error_count = 0

# loop through user input and append to numlist
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break

#check if input is a number, if not throw error and increment error_count
    try:   
        value = float(inp)
        numlist.append(value)
    except:
        error_count = error_count + 1
        
        if error_count == 3: 
            print('Too many errors. Exiting')
            break
        elif error_count < 3:
            print('Invalid input')
            continue 

#calculate average for given list of numbers
average = sum(numlist) / len(numlist)
print('Average:', average)

