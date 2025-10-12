'''Leetcode - 374

Number guessing game 
I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

'''
def guessNumber(n):
    l, r = 1, n
    
    while True:
        m = (l + r) // 2 
        result = guess(m)
        if result > 0:
            l = m + 1
        elif result < 0:
            r = m - 1
        else:
            retrun m