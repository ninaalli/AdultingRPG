#this will filter through logic based on the user input
from view import View
import random

class Game(object):
    """docstring for Game"""
    def __init__(self):
        super(Game, self).__init__()
        self.player = player
        self.view = View

    def start(self):
        self.view.welcome_to_adulting()
        choice = self.view.login_or_registereduser()
        if choice ==0:
            self.login
            #this will reference above
        elif choice ==1:
            self.register
        else:
            return start

    def create_player(self):
        username = self.view.input_user_name()
        occupation = self.view.occupation()
        marital_status = self.view.marital_status()
        gender = self.view.gender()
        age = self.age ()

        age = start points

    #def login(self):
        while True:
            user_name = self.view.input_user_name
            password = self.view.iput_user_pw

class player_class(object):
        """docstring for player_class"""
    def __init__(self, arg):
        super(player_class, self).__init__()
        self.arg = arg

        self.health = 100
        self.health_max = 100
        self.state = "normal"

    def options(self):
        print ((list(commands.keys()))):
        #how to get info out of a list, it iterates through it
        #dictionary: keys/values
            #key: value, Key: value. key is identifier, value is waht gives it meaning.

    commands={
        "quit": player.quit,
        "options": player.options
        "status": player.status
        }
        #[] defines list
        #{} defines dictionary
        #() defines string - cant search through the list

    def status(self):
        print ("%s's health: %d/%d" %(self.name, self.health,self.health_max"))
        #user can print status will say Nina 100/100 or 56/100

    def cirrhosis(self, liquor):
        damage = min(max(randint(0, self.health) - randint(0,booze.strength(,0),booze.strength))))
            if damage ==0:
                print ("%s avoids %'s damage" % (self.name, self.liquor.name)
            else:
                print ("%'s takes %'s damage" % (self.name, self.liquor.name)
            return self.health <=0

    def clean_clothes(self,clothes):
        if choice in [0,1,2,3]:
            return self.health -=3
        else:
            return (clean_clothes)

    class whiskey(self):
        """docstring for whiskey"""
        def __init__(self, name,damage):
            self.name=whiskey
            self.damage=3

    class beer(self):
        """docstring for beer"""
        def __init__(self, name, damage):
            self.name=beer
            self.damage=2

    class tequila(self):
        """docstring for self"""
        def __init__(self, name,damage):
            self.name=tequila
            self.damage=1

    class Play(object):
        """docstring for Play"""
        def __init__(self, arg):
            super(Play, self).__init__()
            self.
