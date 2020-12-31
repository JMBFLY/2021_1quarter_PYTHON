class HUMAN:
    __name = "파이썬"

    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 0

    def show(self):
        print(self.__name)


me = HUMAN(10, 100, 'red', 2, 4)
print(me.age)
print(me.height)
print(me.color)
print(me.xpos)
print(me.ypos)
print(me.velocity)
me.show()
print(me.show())
