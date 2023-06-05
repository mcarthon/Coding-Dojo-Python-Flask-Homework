class Player:

    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    @classmethod
    def get_team(cls, team_list):
        for man in team_list:
            man = Player(man)
            print(type(man))
            print(man.name)
            print(man.age)
            print(man.position)
            print(man.team)
        return team_list

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

team_list = [kevin, jason, kyrie]
Player.get_team(team_list)
