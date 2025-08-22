class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    #Методы класса
    def action(self):
        print(f'{self.name} base action!!')

kirito = Hero(name='Kirito', lvl=100, hp=1000)


asuna = Hero(name='Asuna', lvl=100, hp=900)
num = 123
string = "text"
array = [1, 2, 3, 4, 5]
tuple_my = (1, 2, 3, 4, 5)


print(type(asuna))
print(type(kirito))

