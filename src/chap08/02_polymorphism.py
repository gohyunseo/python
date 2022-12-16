# 다형성(Polymorphism)

class Suit:
    pass


class ArmorSuit:
    def armor(self):
        print('armored')

class IronMan(ArmorSuit):
    pass


def get_armored(suit):
    suit.armor()

if __name__ =="__main__":
    suit = ArmorSuit()
    get_armored(suit)

    print("================")

    iron_man = IronMan()
    get_armored(iron_man)

    suit = Suit()
    get_armored(suit) #get_arored(suit) # error