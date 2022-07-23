class test:
    static_variable = 25 # Access through class
print(test.static_variable) # prints 5
# Access through an instance
ins = test()
print(ins.static_variable) # still 5
# Change within an instance
ins.static_variable = 14
print(ins.static_variable)
print(test.static_variable)

# Static Method : Use @staticmethod
class sample_shape:

    @staticmethod
    def msgg(msg):
        print(msg)
        print("Triangles")

sample_shape.msgg("Welcome to sample shape class")
