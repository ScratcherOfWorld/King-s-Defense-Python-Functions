class Card:
    def __init__(self, name, coins_cost, gems_cost):
        self.name = name
        self.coins_cost = coins_cost
        self.gems_cost = gems_cost

cards = [Card("Wizard", 200,0),
         Card("Skeleton", 100,0),
         Card("Fairy", 1,0),
         Card("Meteor Swarm", 50,0),
         Card("Arrows", 50,0),
         Card("Siege Tower", 1,0),
         Card("Lightning", 1,0),
         Card("Archer", 1,0),
         Card("Paladin", 1,0)]
