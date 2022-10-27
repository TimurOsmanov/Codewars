# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or
# other items. We want to create the text that should be displayed next to such an item.
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes(['a', 'd', 'a']))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def likes(names):
#     output = {
#         0: "no one likes this",
#         1: "{} likes this",
#         2: "{} and {} like this",
#         3: "{}, {} and {} like this",
#         4: "{}, {} and {others} others like this",
#     }
#
#     count = len(names)
#
#     return output[min(4, count)].format(*names[:3], others=count - 2)
#
#
# print(likes(['a', 'd', 'a']))
