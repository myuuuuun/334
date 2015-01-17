# -*- coding: utf-8 -*-
import math
import random
import sys
sys.setrecursionlimit(10000)


def Nandeya(n, flag_3, flag_33):
    v = random.randint(1,6)

    if flag_33:
        if v == 4:
            return n
        elif v == 3:
            return Nandeya(n+1, False, True)
        return Nandeya(n+1, True, False)
    
    if flag_3:
        if v == 3:
            return Nandeya(n+1, False, True)
        return Nandeya(n+1, False, False)

    if v == 3:
        return Nandeya(n+1, True, False)

    return Nandeya(n+1, False, False)


if __name__ == "__main__":
    list = [0 for x in range(1000)]
    for i in range(len(list)):
        try:
            list[i] = Nandeya(1, False, False)

        except RuntimeError:
            print "{0}回目にRuntimeError発生".format(i+1)
            list[i] = Nandeya(1, False, False)

    print list
    print sum(list)/len(list)


