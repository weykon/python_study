# If, Elif and Else one liner
x = 200

var = {x < 190: "Condition one satisfied",
       x != 200: "Condition two satisfied"}.get(True, "Condition third satisfied")

print(var)