# Create a function that differentiates a polynomial for a given value of x.
#
# Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.
#
# Assumptions:
# There will be a coefficient near each x, unless the coefficient equals 1 or -1.
# There will be an exponent near each x, unless the exponent equals 0 or 1.
# All exponents will be greater or equal to zero
# differenatiate("12x+2", 3)      ==>   returns 12
# differenatiate("x^2+3x+2", 3)   ==>   returns 9
def differentiate(equation, point):
    c = list(map(lambda q:  '+' + q if q[0] != '-' else q, equation.split('+')))
    d = [y for x in c for y in x.split('-') if 'x' in y]
    e = list(map(lambda u: '-' + u if u[0] != '+' else u, d))
    f = list(map(lambda l: [z for z in l.split('x')], e))
    answer, res = [], 0
    for x in f:
        temp = [1] if x[0] == '+' else [-1] if x[0] == '-' else [int(x[0])]
        if '^' in x[1]:
            a, b = x[1].split('^')
            temp.append(int(b))
        else:
            temp.append(1)
        answer.append(temp)
    for x in answer:
        res += x[1] * point**(x[1] - 1) * x[0]
    return res


print(differentiate("-5x^2+10x+4", 3))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# from collections import defaultdict
# import re
#
# P = re.compile(r'\+?(-?\d*)(x\^?)?(\d*)')
#
# def differentiate(eq, x):
#
#     derivate = defaultdict(int)
#     for coef,var,exp in P.findall(eq):
#         exp  = int(exp or var and '1' or '0')
#         coef = int(coef!='-' and coef or coef and '-1' or '1')
#
#         if exp: derivate[exp-1] += exp * coef
#
#     return sum(coef * x**exp for exp,coef in derivate.items())
