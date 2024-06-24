#ask user for file name
file_name = input('Enter the file name: ')

#error handling for invalid file name
try:
    file_handler = open(file_name)
except: 
    print('File cannot be opened: ', file_name)
    exit()

#set count of lines to 0
line_count = 0 

for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[1])
    line_count = line_count + 1

total_line = str(line_count)
print('There were ' + total_line + ' lines in the file with From as the first word')