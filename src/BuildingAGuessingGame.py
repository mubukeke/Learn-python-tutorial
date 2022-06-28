
secret_word = "giraffe"
guess = ""
guess_count = 0   # 玩家当前猜的次数
guess_limit = 3   # 玩家总共可以猜的次数
out_of_guess = False   # 表示玩家次数已尽，结束游戏

def guess_word(secretword):
    global guess
    guess_right = False
    while not guess_right:
        guess = input("Enter your guess word:(Tips it's an animal.)")
        if guess == secretword:
            guess_right = True
            print("Congratulations. You are right.")
        else:
            print("Sorry. You are wrong.\nPlease try again.")


def guessWord(secret_word_):
    global guess
    global guess_count
    global guess_limit
    global out_of_guess

    guess = input("Enter guess:")
    while guess != secret_word_:
        if out_of_guess:
            break
        guess_count += 1
        if guess_count == guess_limit:
            print("You out of guess")
            out_of_guess = True
        else:
            guess = input("Enter guess:")


def guessWordOfficial(secret_word_guess):
    global guess
    global guess_count
    global guess_limit
    global out_of_guess

    while guess != secret_word_guess and not out_of_guess:
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_guess = True


# guess_word(secret_word)
# guessWord(secret_word)
guessWordOfficial(secret_word)
if out_of_guess:
    print("Out of guesses, YOU LOSE!")
else:
    print("You Win!")
