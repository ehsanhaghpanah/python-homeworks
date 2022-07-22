#
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.
#

from game import Game
from game import CheckResult

#
# tries to parse provided string as an integer
#
# @param    text : a string representing an integer number
# @return   an integer if possible otherwise none
#
def try_parse(text: str) -> int:
    try:
        return int(text)
    except:
        return None

#
# tries to get an integer number from input
#
# @param    i_msg : input function prompt message
# @return   an integer if possible otherwise none
#
def get_int(i_msg: str) -> int:
    rs = try_parse(input(i_msg))
    if (rs == None):
        print("ERROR: Not a Valid Integer Number, Returning None")
    return rs

#
# main loop
def main_run(lower_bound: int, upper_bound: int, quit_key: str) -> None:
    print("----- pythonic interactive game -----")

    lb = lower_bound if (lower_bound != None) else get_int("give me the lower bound = ")
    ub = upper_bound if (upper_bound != None) else get_int("give me the upper bound = ")
    if lb >= ub:
        print("the lower bound must be less than the upper bound!")
        exit()

    qk = "q" if (quit_key == None) else quit_key

    print("----- game started -----")

    # initializing and computation
    gm = Game(lb, ub)
    while True: #{
        ky = input(f"give me your guess, an integer between {gm.lower_bound} and {gm.upper_bound}, '{qk}' to quit = ")
        if ky == qk:
            print("game quited, bye!")
            break

        gi = try_parse(ky)
        if gi == None:
            continue

        cs = gm.check(gi)
        if cs == CheckResult.STOP:
            print("WOW! your guess is correct. game is over!")
            break
        elif cs == CheckResult.MORE:
            print("not match, GO LOWER!")
        else:
            print("not match, GO UPPER!")
    #}

#
# calling main function
main_run(1, 100, '0')


# or just 
# main_run(None, None, None)