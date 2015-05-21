def sleep_in(weekday, vacation):
    '''weekday - boolean; vacation - boolean
    The parameter weekday is True if it is a weekday, and the
    parameter vacation is True if we are on vacation. We sleep
    in if it is not a weekday or we're on vacation.

    Return True if we sleep in.
    '''
    sleepIn = True if (weekday == False) or (vacation == True) else False
    return sleepIn

def monkey_trouble(a_smile, b_smile):
    '''We have two monkeys, a and b, and the parameters a_smile and b_smile
    indicate if each is smiling. We are in trouble if they are both smiling or
    if neither of them is smiling.

    Return True if we are in trouble.
    '''
    return (True if (a_smile == b_smile) else False)


if __name__ == '__main__':
    #tests for sleep_in method
    assert(sleep_in(False, False) == True)
    assert(sleep_in(True, False) == False)
    assert(sleep_in(False, True) == True)
    ###
    #tests for monkey_trouble method
    assert(monkey_trouble(True,True) == True)
    assert(monkey_trouble(False, False) == True)
    assert(monkey_trouble(True, False) == False)

    input("Press Enter to close") # Python 3 keeps cmd window open

    


