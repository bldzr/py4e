#ask user for file name
file_name = input('Enter the file name: ')

#error handling for invalid file name
try:
    file_handler = open(file_name)
except: 
    if file_name == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    else:
        print('File cannot be opened: ', file_name)
        exit()

#set count and to 0
count = 0 
total_spam = 0

#search for matching string
for line in file_handler:
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    count = count + 1
    line = line.rstrip()
    number = float(line[20:])
    total_spam = total_spam + number

#display results
print ('Average spam confidence:', total_spam/count)

#close files
file_handler.close()
