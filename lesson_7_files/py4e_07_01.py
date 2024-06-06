#ask user for file name
file_name = input('Enter the file name: ')

#error handling for invalid file name
try:
    file_handler = open(file_name)
except: 
    print('File cannot be opened: ', file_name)
    exit()

#print lines as upper case 
for line in file_handler:
    line = line.rstrip()
    print(line.upper())


#close files
file_handler.close()
