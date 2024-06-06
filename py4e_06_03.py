#define count letters function. Should accept a word and what letter you want to count.
def count_letters(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

#ask user for input for word and letter
word = input ('Enter a word: ')
letter = input ('Enter a letter you want to count: ')

#return count of letter in word
print (count_letters(word, letter))
