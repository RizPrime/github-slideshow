import random

print("Welcome to Snake, Water and Gun battle!")
matches = 10
usr = 0
comp = 0
options = ["Snake", "Water", "Gun"]


def result(c, u):
    if c == "Snake" and u == "w":
        return 0, 1
    elif c == "Snake" and u == "g":
        return 1, 0
    elif c == "Water" and u == "s":
        return 1, 0
    elif c == "Water" and u == "g":
        return 0, 1
    elif c == "Gun" and u == "s":
        return 0, 1
    elif c == "Gun" and u == "w":
        return 1, 0
    else:
        return 0, 0


while matches > 0:
    cmp_str = random.choice(options)
    print(f"Enter s for Snake, w for Water and g for Gun, {matches} matches left:", end=" ")
    usr_str = input()
    print(f"Computer chose {cmp_str}.")
    ans = result(cmp_str, usr_str)
    matches = matches - 1
    usr = usr + ans[0]
    comp = comp + ans[1]

if usr > comp:
    print(f"You win by {usr} points.")
else:
    print(f"Computer wins by {comp} points.")