#!/usr/bin/env python

import math


def make_chocolate(small, big, goal):
    return make_chocolate2(small, big, goal)


def make_chocolate1(small, big, goal):
    # 99 200 100 = -11

    # we could use 20 bars
    # but we have 200
    # pick the minimum... 20 ... thats the number of big bars you'd use


    # how many big bars can we possibly utilize
    could_use_big_bars = math.floor(goal / 5)

    # but we only have [big] amount of them, so take the min of the two
    big_bars_used = min(big, could_use_big_bars)

    # now calculate how many small bars we need after using as many big
    # bars as we wanted
    goal_from_small_bars = goal - (5 * big_bars_used)

    # if we don't have enough...
    if small < goal_from_small_bars:
        return -1

    return goal_from_small_bars


def make_chocolate2(small, big, goal):
    # 99 99 99

    # 99 / 5 ... .asking for the remainder

    if big*5 >= goal:
        # we have more big bars than we can fully use
        # so find the "mod" remainder after using all big bars
        # AKA we want the remainder of GOAL/SIZE_OF_BIG (which would give us number of big
        # bars used... the remainder is the number of small bars to use)
        remainder = goal % 5
    else:
        # we used all our big bars and still need more
        remainder = goal - (big*5)

    if remainder > small:
        # we don't have enough
        return -1

    return remainder


if __name__ == '__main__':
    # check
    print(make_chocolate(4, 1, 9))  # 4
    print(make_chocolate(4, 1, 10))  # -1
    print(make_chocolate(4, 1, 7))  # 2
    print(make_chocolate(6, 2, 7))  # 2
    print(make_chocolate(4, 1, 7))  # 2
    print(make_chocolate(1, 2, 7))  # -1
    print(make_chocolate(6, 1, 10))  # 5
    print(make_chocolate(60, 100, 550))  # 50
    print(make_chocolate(100, 1000000, 5000006))  # 6
    print(make_chocolate(7, 2, 13))  # 3


# implement more tests
