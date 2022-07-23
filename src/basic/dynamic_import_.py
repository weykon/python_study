#implementation
#fabs() method is defined in the math module which returns the #absolute value of a number
math_score = __import__('math', globals(), locals(), [], 0)
print(math_score.fabs(-17.4))
