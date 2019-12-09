#input("Welcome to 'Initiative Tracker v.0.1")
#creature_count = input ("How many unique creatures are we dealing with today?: ")
#double_check = input(creature_count + ", is that right? ('y' or 'n') ")

class mob:
    def __init__(self, name, initiative, ac):
        self.name = name
        self.initiative = initiative
        self.ac = ac

    def full(self):
        return '{}, Initiative: {}, AC: {}'.format(self.name, self.initiative, self.ac)
        

mob1 = mob("Abnemooor", "10", "15")
mob2 = mob("Brienne", "18", "16")

print(mob1.full())
print(mob2.full())
