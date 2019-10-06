int_list = list(map(int, input().split()))
command_list = list(map(int, input().split()))

for command in command_list:
    if command % 2 == 0:
        for i in range(len(int_list)):
            if int_list[i] % 2 == 0:
                int_list[i] = int_list[i] * abs(command)
    else:
        for i in range(len(int_list)):
            if int_list[i] % 2 != 0:
                int_list[i] = int_list[i] // abs(command)
    if command > 0:
        for i in range(len(int_list)):
            if int_list[i] > 0:
                int_list[i] = int_list[i] + command
    else:
        for i in range(len(int_list)):
            if int_list[i] < 0:
                int_list[i] = int_list[i] + command

print(int_list)