def alternate_letters(word):
    new_word = word[::2]
    print(new_word)
    return new_word

assert alternate_letters("Апельсин") == "Аплн"
