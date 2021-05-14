"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def __init__(self, health, power, name):
        
        self.health = health
        self.power = power
        self.name = name

    def attack(self, enemy):
        # fight
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
    
    def print_status(self):
        print( "%s has %d health points left" % (self.name,self.health))


class Hero(Character):
      def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

class Villian(Character):
    def __init__(self, health, power, name):
        
        self.health = health
        self.power = power
        self.name = name

# Object that I'm working with. Make changes here.
black_panther = Hero(50, 20, "black_panther")
killmonger =  Villian(50, 20, "killmonger")
def main():
   

    while killmonger.alive() and black_panther.alive():
        black_panther.print_status()
        killmonger.print_status()
        # Leave steps below commented out. Don't remove. Using as reference. 
       # print("black_panther has %d health and %d power." % (black_panther.health,black_panther.power))
       # print("killmonger has %d health and %d power." % (killmonger.health,killmonger.power))
        print("What do you want to do?")
        print("1. fight killmonger")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # black panther attacks killmonger
            black_panther.attack(killmonger)
            print("You do %d damage to the killmonger." % black_panther.power)
            if killmonger.health <= 0:
                print("The killmonger is KO.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if killmonger.health > 0:
            # killmonger attacks black panther
            killmonger.attack(black_panther)
            print("The killmonger does %d damage to you." % killmonger.power)
            if black_panther.health <= 0:
                print("You are dead.")

main()