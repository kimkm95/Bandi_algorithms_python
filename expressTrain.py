# D = 325
# H = 16.0 / 60.0
# print(int(D / H)) 

# D = 42195
# S = ((121*60) + 39)

# print(int(D / S))


def celsius2fahrenheit(C):
    F = 9/5 * C + 32
    return F
print(celsius2fahrenheit(19.4))
print(round(celsius2fahrenheit(19.4),1))