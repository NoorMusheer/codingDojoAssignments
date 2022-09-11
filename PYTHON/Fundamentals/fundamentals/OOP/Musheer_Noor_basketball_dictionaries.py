players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]

class Player:
    new_list_of_player_objects = []
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    @classmethod
    def get_team(cls,team_list):
        for each_element in team_list:
            new_player = Player(each_element)
            cls.new_list_of_player_objects.append(new_player)
            


player_kevin = Player({"name": "Kevin Durant", "age": 34,"position": "Small forward", "team": "Brooklyn Nets"})
player_jason = Player({"name": "Jason Tatum", "age": 24,"position": "Small forward", "team": "Boston Celtics"})
player_kyrie = Player({"name": "Kyrie Irving", "age": 32,"position": "Point Guard", "team": "Brooklyn Nets"})


new_team=[]
for element in players:
    player = Player(element)
    new_team.append(player)

print("Challenge 3 results: ")
print(new_team)


Player.get_team(players)
print("Bonus Challenge results: ")
print(Player.new_list_of_player_objects)

