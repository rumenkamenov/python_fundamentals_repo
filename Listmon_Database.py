class Listmon:
    def __init__(self, playerName, score, numberOfGames):
        self.playerName = playerName
        self.score = score
        self.numberOfGames = numberOfGames


players = []

while True:
    data = input()
    if data.split(' -> ')[0] == "report":
        break

    name = data.split(' -> ')[0]
    games_list = list(map(int, data.split(' -> ')[1].split(', ')))
    score = sum(games_list)
    games_number = len(games_list)

    player = Listmon(name, score, games_number)
    players.append(player)

data = input()

while not data.split()[0] == 'end':
    if data.split()[0] == 'score':
        if data.split()[1] == 'ascending':
            formatted_list = sorted(players, key=lambda obj: (obj.score, obj.playerName))
            for inst in formatted_list:
                print(f'{inst.playerName}: {inst.score}')
        else:
            formatted_list = sorted(players, key=lambda obj: (-obj.score, obj.playerName))
            for inst in formatted_list:
                print(f'{inst.playerName}: {inst.score}')

    if data.split()[0] == 'numberOfGames':
        if data.split()[1] == 'ascending':
            formatted_list = sorted(players, key=lambda obj: (obj.numberOfGames, obj.playerName))
            for inst in formatted_list:
                print(f'{inst.playerName}: {inst.numberOfGames}')
        else:
            formatted_list = sorted(players, key=lambda obj: (-obj.numberOfGames, obj.playerName))
            for inst in formatted_list:
                print(f'{inst.playerName}: {inst.numberOfGames}')

    data = input()