entry = input()

dict_dict = {}

for i in range(len(entry)):
    if entry[i] in dict_dict.keys():
        dict_dict[entry[i]].append(i)
    else:
        dict_dict[entry[i]] = [i]

for key, value in dict_dict.items():
    print(f"{key}:{'/'.join(list(map(str,value)))}")