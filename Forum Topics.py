data = input()
forum_dict = {}


while not data == "filter":
    topic = data.split(' -> ')[0]
    hastags = data.split(' ')[1].split(', ')

    if topic in forum_dict.keys():
        forum_dict[topic].extend(hastags)
    else:
        forum_dict[topic] = hastags

    data = input()

hastags_req = input().split(', ')

for topic, hastags in forum_dict.items():

    unique_tags_list = sorted(set(hastags), key=hastags.index)
    forum_dict[topic] = unique_tags_list
    hastags_req_set = set(hastags_req)
    if hastags_req_set.issubset(hastags):
        print(f"{topic} | #{', #'.join(unique_tags_list)}")
