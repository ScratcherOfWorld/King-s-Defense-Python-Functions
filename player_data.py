import data_formatter
class PlayerStaticData:
    def __init__(self, username):
        self.username = username
        self.gems=100
        self.coins=10
        self.points=0
        self.cards=[]

    def get_dict(self): #Dictionary is used to store values in file.
        return {"Username":self.username,
                "Gems":self.gems,
                "Coins":self.coins,
                "Points":self.points,
                "Cards":self.cards}
    
    def from_dict(self, dictionary_in): #Use when reading from file.
        self.username=dictionary_in["Username"]
        self.gems=dictionary_in["Gems"]
        self.coins=dictionary_in["Coins"]
        self.points=dictionary_in["Points"]
        self.cards=dictionary_in["Cards"]

    def get_values(self):
        string = ''.join([data_formatter.make_text_set_length(str(self.gems),6),
                          data_formatter.make_text_set_length(str(self.coins),6),
                          data_formatter.make_text_set_length(str(self.points),6),
                          ''.join(self.cards)])
        return string
                          
                    
