
is_male = True
is_tall = False

if is_male or is_tall:   # if statement with multi-conditions using keywords: or / and
    print("You are a male or tall or both.")
else:
    print("You neither male nor tall.")


if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not is_tall:    # elif 多条件分支   not 非
    print("You are a short male.")
elif not is_male and is_tall:
    print("You are not a male but a tall.")
else:
    print("You are short female.")