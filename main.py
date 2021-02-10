import math
def f(x):
    if x < 143:
        return(x**4-x**2+80)
    elif 143 <= x < 154:
       return (x**5-5*x+89)
    elif 154 <= x < 194:
        return (math.e**(x**6+x**7)+(x**6/4))
    elif x >= 194:
        return (math.e**x**8-36*x**2-24)

x = int(input("Enter X: "))
print('%e' % f(x))