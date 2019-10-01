data = input()
media_dict = {}

while not data == "drop the media":
    comand = data.split()[0]
    postname = data.split()[1]

    if comand == 'post':
        media_dict[postname] = {'likes': 0, 'dislikes': 0, 'comments': []}

    elif comand == 'like':
        if postname in media_dict.keys():
            media_dict[postname]['likes'] += 1

    elif comand == 'dislike':
        if postname in media_dict.keys():
            media_dict[postname]['dislikes'] += 1
    elif comand == 'comment':
        author = data.split()[2]
        content = data.split()[3]
        if postname in media_dict.keys():
            comment = {author:content}
            media_dict[postname]['comments'].append(comment)


    data =input()

for postname, post_data in media_dict.items():
    print(f"Post: {postname} | Likes: {post_data['likes']} | Dislikes: {post_data['dislikes']}")
    print('Comments:')
    if not post_data['comments']:
        print('None')
        continue
    for comment in post_data['comments']:
        for current_post in comment:
            print(f'*  {current_post}: {comment[current_post]}')

    #[print(f'*  {author}: {content}') for author, content in post_data['comments'].items()]