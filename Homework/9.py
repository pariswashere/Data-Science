class exp:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        result = eval(self.expression)
        return result

    def display(self):
        print("Expression:", self.expression)
        print("Result:", self.solve())

expr = input("Enter a mathematical expression: ")

solver = exp(expr)
solver.display()