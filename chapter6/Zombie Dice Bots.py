import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class Shortgun:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class MyZombieOneToFour:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        roll=4
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            roll=roll-1
            if shotgun < 2 and roll>0:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class randomChance:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
       

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        
        while diceRollResults is not None and random.randint(0,1)==0:
                diceRollResults = zombiedice.roll() # roll again
class MoreShotGun:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        brain=0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brain += diceRollResults['brain']
            if shotgun < brain:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    Shortgun(name='Zombie Ashu'),
    MyZombieOneToFour(name='Zombie Riya'),
    randomChance(name='Zombie Rishu'),
    MoreShotGun(name='Zombie dice')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)