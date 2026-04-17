class dad:

    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive

    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggressive", self.aggressive)

class son(dad):
    
    def __init__(self, name, age, eyes, aggressive):
        self.name = name
        self.age = age
        dad.__init__(self, eyes, aggressive)

    def display(self):
        print("Your name is :", self.name)
        print("Your age is :", self.age)
        print("Your eyes are : ", self.eyes)
        print("You are aggressive :", self.aggressive)


s = son("Chris", 10, "Blue", True)

s.display()
    
