class Employee :

    def __init__(self):
        print("Employee class created.")

    def __del__(self):
        print("Employee deleted.")

obj = Employee()
del obj