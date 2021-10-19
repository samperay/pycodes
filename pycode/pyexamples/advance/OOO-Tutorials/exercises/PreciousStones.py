# EXERCISE - ATTRIBUTES AND METHODS

# Write an object oriented program to create a precious stone.
# Not more than 5 precious stones can be held in possession at a
# given point of time. If there are more than 5 precious stones,
# delete the first stone and store the new one.

class PreciousStones:
    numberOfPreciousStones = 0
    preciousStonesBucket = []

    def __init__(self, name):
        self.name = name
        PreciousStones.numberOfPreciousStones += 1
        if PreciousStones.numberOfPreciousStones <= 5:
            PreciousStones.preciousStonesBucket.append(self.name)
        else:
            del PreciousStones.preciousStonesBucket[0]
            PreciousStones.preciousStonesBucket.append(self.name)

    @staticmethod
    def displayPreciousStones():
        print("Total precious stones in the bucket: ")
        for each_stone in PreciousStones.preciousStonesBucket:
            print(each_stone)


stone1 = PreciousStones("Ruby")
stone2 = PreciousStones("Emerald")
stone3 = PreciousStones("Sapphire")
stone4 = PreciousStones("Diamond")
stone5 = PreciousStones("Amber")
stone5.displayPreciousStones()
stone6 = PreciousStones("oxy")
stone6.displayPreciousStones()
