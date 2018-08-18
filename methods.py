class Fighter:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.damage = 10

    def __str__(self):
        return '{} : {}' .format(self.name,self.health)

    def attack(self, other):
        other.health -= self.damage
        print('{} attacks {}!'. format (self.name, other.name))
        print('{} loses {} health!'.format(other.name, self.damage))

ryu = Fighter("Ryu")
qazi =Fighter("Qazi")

print (ryu)
print (qazi)

ryu.attack(qazi)
print(qazi)
