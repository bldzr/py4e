#ask user for file name
file_name = input('Enter the file name: ')

#error handling for invalid file name
try:
    file_handler = open(file_name)
except: 
    print('File cannot be opened: ', file_name)
    exit()

#set count to 0 
count = 0

#count number of lines that start with 'Subject:' 
for line in file_handler:
    if line.startswith('Subject:'):
        count = count + 1

fout= open('output.txt', 'a')

#display results
print ('There were', count, 'subject lines in', file_name)

#also write results to file output.txt
fout.write(f'There were {count} subject lines in {file_name}.\n')

#close files
file_handler.close()
fout.close()    