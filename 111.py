import math 
def quadratic(a,b,c):
    if b**2-4*a*c < 0:
        print('无解')
        return
    x1=(-b + math.sqrt(b**2-4*a*c))/ (2*a)
    x2= (-b - math.sqrt(b**2-4*a*c))/ (2*a)
    return x1,x2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))