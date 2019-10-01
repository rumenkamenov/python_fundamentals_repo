command = input()

equipment_list = []

while command != "Fight!":
    command_n = command.split()[0]
    item = command.split()[1]

    if command_n != 'Buy' and command_n != 'Trash' and command_n != 'Repair' and command_n != 'Upgrade':
        for i in command.split():
            equipment_list.append(i)

    elif command_n == "Buy":
        if command_n == 'Buy' and item not in equipment_list:
            equipment_list.append(item)


    elif command_n == 'Trash' and item in equipment_list:
        equipment_list.remove(item)

    elif command_n == "Repair":
        equipment_list.append(item)
        if item == item:
            equipment_list.remove(item)

    elif command_n == 'Upgrade':
        if item.split('-')[0] in equipment_list:
            new_pos = equipment_list.index(item.split('-')[0])
            item = item.replace('-', ':')
            equipment_list.insert(new_pos + 1, item)

    command = input()

print(' '.join(equipment_list))

