text = input()
case = input()

text_list = list(text)

sum = 0

for letter in text_list:
    if letter.islower():
        if case == "LOWERCASE":
            sum += ord(letter)
    if letter.isupper():
        if case == "UPPERCASE":
            sum += ord(letter)
print(f'The total sum is: {sum}')