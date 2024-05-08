word = 'Halkin'
new_word = ''
for a in word:
    new_word = a + new_word

if new_word == word:
    print('palindrome')
else:
    print(f'word = {word} is not palindrome')