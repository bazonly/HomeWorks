import math


def theQuadraticEquation(A, B, C):

    D = pow(B,2)-4*A*C
    if D>0:
        x1 = (-B-math.sqrt(D))/(2*A)
        x2 = (-B+math.sqrt(D))/(2*A)
        print(f'x1= {x1}\nx2= {x2}')
        pass
    elif D==0:
        x=-B/(2*A)
        print(f'x= {x}')
        pass
    else:
        print('решений нет')
        pass

if __name__ == '__main__':
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    C = int(input('Enter C: '))
    theQuadraticEquation(A, B, C)

