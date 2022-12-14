# The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him.
# Gabriel thunders to the pope:
# Gather all of the learned men in Pisa, especially Leonardo Fibonacci. In order for the crusades in the holy lands
# to be successful, these men must calculate the millionth number in Fibonacci's recurrence.
# Fail to do this, and your armies will never reclaim the holy land. It is His will.
# The angel then vanishes in an explosion of white light.
# Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.
# He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment
# in history, he cannot represent this number. If he only knew about the invention of zero,
# it might make this sort of thing easier.
# He decides to go back to bed. He consoles himself, The Lord would never challenge me thus;
# this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.
# Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul),
# but they would never reclaim the holy land as he desired.
# In this kata you will have to calculate fib(n) where:
# fib(0) := 0
# fib(1) := 1
# fin(n + 2) := fib(n + 1) + fib(n)
# Write an algorithm that can handle n up to 2000000.
# Your algorithm must output the exact integer answer, to full precision.
# Also, it must correctly handle negative numbers as input.
# HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n)
# if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.
def matrix_mul(a, b):
    return [[
        a[0][0] * b[0][0] + a[0][1] * b[1][0],
        a[0][0] * b[0][1] + a[0][1] * b[1][1]
    ], [
        a[1][0] * b[0][0] + a[1][1] * b[1][0],
        a[1][0] * b[0][1] + a[1][1] * b[1][1]
    ]]


def fast_pow(p):
    t, m = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
    while p:
        if p % 2:
            t = matrix_mul(t, m)
        m = matrix_mul(m, m)
        p //= 2
    return t


def fib(n):
    return fast_pow(n)[1][0] if n > 0 else (fast_pow(abs(n))[1][0] if n % 2 else -fast_pow(abs(n))[1][0])


print(fib(-4))

##############################
# fast pow algo
# def pow(a, p):
#     res = 1
#     a = a
#     while p:
#         if p % 2:
#             res *= a
#         a *= a
#         p //= 2
#     return res
# print(pow(2, 5))
#
########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def fib(n):
#   if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
#   a = b = x = 1
#   c = y = 0
#   while n:
#     if n % 2 == 0:
#       (a, b, c) = (a * a + b * b,
#                    a * b + b * c,
#                    b * b + c * c)
#       n /= 2
#     else:
#       (x, y) = (a * x + b * y,
#                 b * x + c * y)
#       n -= 1
#   return y
