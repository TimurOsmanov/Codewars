def scramble(s1, s2):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    letter_num = {letter: 0 for letter in alp}
    for x in s1:
        letter_num[x] += 1
    for x1 in s2:
        letter_num[x1] -= 1
    return False if any(letter_num[x2] < 0 for x2 in alp) else True

# def scramble(s1,s2):
#     return all( s1.count(x) >= s2.count(x) for x in set(s2))

print(scramble('rkqodlw', 'world'))
