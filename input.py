import pickle

class Player:
    def __init__(self, name, age, location, income, family, job):
        self.name = name
        self.age = age
        self.location = location
        self.income = income
        self.family = family
        self.job = job
        self.inventory = []
        self.attributes = {}
        self.skills = {}
    
    def add_item(self, item):  # 아이템 추가 메서드
        self.inventory.append(item)
    
    def remove_item(self, item):  # 아이템 삭제 메서드
        if item in self.inventory:
            self.inventory.remove(item)

def create_character():
    name = input("What's your character's name? ")
    age = int(input("How old is your character? "))
    location = input("Where does your character live? ")
    income = int(input("What's your character's income level? "))
    family = input("Who is in your character's family? ")
    job = input("What's your character's job? ")

    player = Player(name, age, location, income, family, job)
    
    if player.job == "Engineer":
        player.skills["Crafting"] = True
    if player.age > 50:
        player.attributes["Respected"] = True
    
    return player

def save_game(player):
    with open('savegame.pkl', 'wb') as f:
        pickle.dump(player, f)
    
def load_game():
    with open('savegame.pkl', 'rb') as f:
        player = pickle.load(f)
    return player

    