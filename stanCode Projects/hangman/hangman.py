"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    The program demonstrate the classic game 'hangman'. The user have n_turns of lives for user to
    guess a random word picked by the program.
    The user will guess one letter at a time.
    If the user have the wrong guess, he/she will lose a life.
    """

    # decide the word
    word=random_word()
    turn = N_TURNS
    blank = ''

    # show how many letters in the word
    for i in range(len(word)):
        blank+='-'
    print('The word looks like '+blank)
    print('You have '+str(turn)+ ' guesses left')

    old_ans = blank

    while True:
        m = input('Your guess: ')
        m = m.upper()

        # lose
        if turn == 0:
            print('You are completely hung!')
            print('The word was: ' + word)
            break

        # illegal format
        if not m.isalpha() or len(m)!=1:
            print('Illegal format')
            continue

        # find m
        new_ans = hang(word,m,old_ans)

        # wrong guess
        if new_ans == old_ans:
            turn -= 1
            print('There\'s no '+m+'\'s in the word.')

        print('The word looks like '+new_ans)
        print('You have '+ str(turn)+ ' guesses left.')

        old_ans = new_ans

        if new_ans == word:
            print('You are correct!')
            print('The word was: '+ word)
            break


def hang(word, m,old_ans):
    new_ans=''
    # no m in the word
    if word.find(m) == -1:
        return old_ans

    # m is in the word
    else:
        for k in range(len(word)):

            # find m
            if word[k]!=m:
                if old_ans[k].isalpha():
                    new_ans += old_ans[k]
                else:
                    new_ans += '-'
            else:
                new_ans+=m
        return new_ans





def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"










#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
