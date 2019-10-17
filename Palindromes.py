text = input().split(' ')
list_palindrom = []

for word in text:
    if word == word[::-1]:
        list_palindrom.append(word)

print(', '.join(sorted((set(list_palindrom)), key=str.lower)))