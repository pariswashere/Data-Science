class Square:

    def __init__(self):
        self.__side = 10


    def area(self):
        print("Side :", self.__side)
        print("Area :", self.__side**2)


osquare = Square()

osquare.__side = 15

osquare.area()