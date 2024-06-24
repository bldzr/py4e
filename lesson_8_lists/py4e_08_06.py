# create empty list and set error_count to 0
numlist = list()

# loop through user input and append to numlist
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break

#check if input is a number, if not throw error 
    try:   
        value = float(inp)
        numlist.append(value)
    except:
        print('Invalid input')
        continue 

#calculate max and min for list of numbers
print('Maximum: ', max(numlist))
print('Minimum: ', min(numlist))
