name1 = input("What's your name: ")
name2 = input("What's your name: ")
match = (len(name1) * len(name2)) % 11
print(f"[{'#' * match}{' ' * (10 - match)}]")
if match >= 0 and match <= 2:
    print("You're a terrible match!")
elif match >= 3 and match <= 5:
    print("You probably shouldn't bother")
elif match >= 6 and match <= 8:
    print("You're a good match")
elif match >= 9 and match <= 10:
    print("You're a perfect match!")
