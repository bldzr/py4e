def count_letters(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
            return count

word = input ('Enter a word: ')
letter = input ('Enter a letter you want to count: ')

print(count_letters(word, letter))
