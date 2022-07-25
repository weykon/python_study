#Example :

#var = lambda x: x * 5

#A lambda function that adds 10 to the number passed in as an #argument, and print the result
x = lambda a, b, c : a * b + c
print(x(5, 6, 8))


#map
numbers = [1,2,3,4,5]
strings = ['s', 't', 'x', 'y', 'z']
mapped_list = list(map(lambda x, y: (x, y), strings, numbers))
print(mapped_list)

#map implementation
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
mod_days = list(map(str.swapcase, days))
print(mod_days)


# 还要list去接住 - -｜｜

#Filter function
marks = [95, 40, 68, 95, 67, 61, 88, 23, 38, 92]
def stud(score):
    return score < 33
fail_list = list(filter(stud, marks))
print(fail_list)