#set smallest variable value to None 
smallest = None

print('Before')

#loop through values in list and set first value to smallest

for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None :
        smallest = value 
    elif value < smallest :
        smallest = value
    print (smallest, value)
print ('After', smallest)

