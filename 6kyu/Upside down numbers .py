# Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same.
# To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same.
# Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.
# Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3,
# because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.
# More examples in the test cases.
# Good luck!
# If you like this Kata, please try
# Simple Prime Streaming
# Life without primes
# Please also try the performance version of this kata at Upside down numbers - Challenge Edition
def upsidedown(x, y):
    dict_ = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    count = 0
    for x in range(int(x), int(y) + 1):
        if len(str(x)) == 1:
            if str(x) in ('0', '1', '8'):
                count += 1
        elif len(str(x)) % 2 == 0:
            if all([num in ('0', '1', '6', '8', '9') for num in str(x)]):
                middle = len(str(x)) // 2
                left, right = str(x)[:middle], str(x)[middle:]
                left = ''.join([dict_[x] for x in left[::-1]])
                if left == right:
                    count += 1
        else:
            if all([num in ('0', '1', '6', '8', '9') for num in str(x)]):
                middle = len(str(x)) // 2
                left, right = str(x)[:middle], str(x)[middle + 1:]
                left = ''.join([dict_[x] for x in left[::-1]])

                if left == right and str(str(x)[middle]) in ('0', '1', '8'):
                    count += 1
    return count


print(upsidedown('100000', '12345678900000000'))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# REV = {'6':'9', '9':'6'}
# BASE = set("01869")
#
# def isReversible(n):
#     s = str(n)
#     return ( not (set(s) - BASE)                                                          # contains only reversible characters
#              and (not len(s)%2 or s[len(s)//2] not in "69")                               # does not contain 6 or 9 right in the middle (only for odd number of digits)
#              and all( REV.get(c, c) == s[-1-i] for i,c in enumerate(s[:len(s)//2]) ))     # symmetric repartition
#
# def solve(a, b):
#     return sum( isReversible(n) for n in range(a,b) )
