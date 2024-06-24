unique_words = list()
file_handle = open('romeo.txt')

for line in file_handle:
    words = line.split()
    for word in words:
        if word in unique_words:
            continue
        else:
            unique_words.append(word)

unique_words.sort()
print(unique_words)


