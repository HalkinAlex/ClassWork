word = ""
seen_characters = set()

while True:
    char = input("Введіть символ (для завершення введіть 'exit'): ")

    if char == 'exit':
        break

    if char in seen_characters:
        print(f"no sequential duplicates allowed, you’ve entered: {word}")
        break

    word += char
    seen_characters.add(char)

    if word == word[::-1]:
        print(f"it’s palindrome: {word}")
        break