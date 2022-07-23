#Class attribute and Instance Attribute
class emp:
    x = 10      #class attribute
    def __init__(self):
        self.name = 'Steve'
        self.salary = 10000

    def display(self):
        print(self.name)
        print(self.salary)

obj_emp = emp()
print("Dictionary conversion:", vars(obj_emp))