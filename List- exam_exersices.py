while True:
    str_line = input()
    if str_line == "stop playing":
        break
    else:
        int_list =list(map(int, str_line.split()))
        #print(int_list)
        int_set_of_list = set(int_list)
        if len(int_list) == len(int_set_of_list):
            sum_list=0
            for i in range(len(int_list)):
                if int_list[i]%2 ==0:
                    int_list[i] += 2
                sum_list += int_list[i]
            print(f"Unique list: {','.join(list(map(str, sorted(int_list))))}")
            print(f"Output: {sum_list/len(int_list):.2f}")
        else:
            sum_list = 0
            for j in range(len(int_list)):
                if int_list[j]%2 != 0:
                    int_list[j] += 3
                sum_list += int_list[j]
            print(f"Non-unique list: {':'.join(list(map(str, sorted(int_list))))}")
            print(f"Output: {sum_list/len(int_list):.2f}")