word = input('Enter a word: ')
reversed_word = str(word)[::-1]

if word == reversed_word:
    print('Given word is a palindrome word.')
else:
    print('Given word is not a palindrome word.')
