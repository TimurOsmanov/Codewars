# The purpose of this kata is to write a program that can do some algebra.
#
# Write a function expand that takes in an expression with a single, one character variable, and expands it.
# The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative,
# x is any single character variable, and n is a natural number.
# If a = 1, no coefficient will be placed in front of the variable.
# If a = -1, a "-" will be placed in front of the variable.
#
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f...
# where a, c, and e are the coefficients of the term, x is the original one character variable
# that was passed in the original expression and b, d, and f,
# are the powers that x is being raised to in each term and are in decreasing order.
#
# If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one,
# the coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included.
# If the power of the term is 0, only the coefficient should be included.
# If the power of the term is 1, the caret and power should be excluded.
import re
from math import factorial


def expand(expr):
    b1, b2, pow_ = re.findall(r'[+-]?\w+', expr)
    b1_pos_neg, b1_num, b1_symb = re.findall(r'[+-]', b1), re.findall(r'\d+', b1), re.findall(r'[a-z]', b1)[0]
    b1_pos_neg, b1_num = '' if b1_pos_neg == [] else b1_pos_neg[0], 1 if b1_num == [] else b1_num[0]
    b1_num = int(str(b1_pos_neg) + str(b1_num))
    sum_ = [factorial(int(pow_)) // (factorial(x) * factorial(int(pow_) - x)) for x in range(int(pow_) + 1)]
    bin_ex = [int(b2) ** x * int(b1_num) ** (int(pow_) - x) * sum_[x] for x in range(int(pow_) + 1)]
    ans = [f"{x}{b1_symb}^{int(pow_) - y}".replace(f"{b1_symb}^1", b1_symb).replace(f"{b1_symb}^0", '')
           for x, y in zip(bin_ex, range(int(pow_) + 1))]
    ans = [x if re.findall(r'\d+', x)[0] != '1' else (x if ans == ['1'] else
                                                      (x if x in ('1', '-1') else x.replace('1', ''))) for x in ans]
    ans[1:] = ['+' + x if x[0] != '-' else x for x in ans[1:]]

    return ''.join(ans)


print(expand("(x-1)^1"))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# import re
#
# P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')
#
# def expand(expr):
#     a,v,b,e = P.findall(expr)[0]
#
#     if e=='0': return '1'
#
#     o   = [int(a!='-' and a or a and '-1' or '1'), int(b)]
#     e,p = int(e), o[:]
#
#     for _ in range(e-1):
#         p.append(0)
#         p = [o[0] * coef + p[i-1]*o[1] for i,coef in enumerate(p)]
#
#     res = '+'.join(f'{coef}{v}^{e-i}' if i!=e else str(coef) for i,coef in enumerate(p) if coef)
#
#     return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-','-')
