import random
class Hang:
    def __init__(self):
        self.equipment_type = ['무기','방어구','악세사리','방어구','무기','방어구']
        self.select = None
    def play(self):

    

    def hang_bronze(self):
        percent=random.randint(1,1000)
        if 0< percent <= 700:
            return 'Normal'
        elif 700 < percent <= 900:
            return 'Grand'
        elif 900 < percent <= 990:
            return 'Rare'
        elif 990 < percent <= 1000:
            return 'Unique'
        
    def hang_silver(self):
        percent=random.randint(1,1000)
        if 0< percent <= 600:
            return 'Normal'
        elif 600 < percent <= 880:
            return 'Grand'
        elif 880 < percent <= 985:
            return 'Rare'
        elif 985 < percent <= 1000:
            return 'Unique'
        
    def hang_gold(self):
        percent=random.randint(1,1000)
        if 0< percent <= 550:
            return 'Normal'
        elif 550 < percent <= 850:
            return 'Grand'
        elif 850 < percent <= 970:
            return 'Rare'
        elif 970 < percent <= 1000:
            return 'Unique'