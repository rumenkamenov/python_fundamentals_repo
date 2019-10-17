text = input()
diamonds = []
first_index = 0
ssecond_index = 0
while True:
    first_index = text.find("<")
    if first_index == -1:
        break;
    second_index = text.find(">")
    if second_index == -1:
        break
    if second_index < first_index:
        text = text[first_index:]
        continue
    diamond = text[first_index+1:second_index]
    text = text[second_index+1:]
    diamonds.append(diamond)
if len(diamonds) > 0:
    for item in diamonds:
        sum = 0
        for index in range(0, len(item)):
            if ord(item[index]) >= 48 and ord(item[index]) <=57:
                number = int(item[index])
                sum = sum + number
        print(f"Found {sum} carat diamond")
else:
    print("Better luck next time")