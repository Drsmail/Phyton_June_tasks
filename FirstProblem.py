# ---------------------------------------
# FIRST PROBLEM
# ---------------------------------------


# More easily understandable way (therefore more pythonic)
#More info here https://stackoverflow.com/questions/40963108/preferred-method-of-checking-for-even-number
# Or here https://stackoverflow.com/questions/1089936/is-faster-than-when-checking-for-odd-numbers
def isEven(number: int) -> bool:
    return number % 2 == 0


# This function is faster because operations like a 'and', 'or', 'xor' work faster.
# Operation '%' uses division and subtraction, so it's slower.
# But this code is harder to read/understand, it's requires comments and is harder to maintain and update.
def fastisEven(number: int) -> bool:
    return not (number & 1)

def printIsEven(number: int, func):
    if func(number):
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")


if __name__ == '__main__':
    printIsEven(4, fastisEven)
    printIsEven(3, isEven)
