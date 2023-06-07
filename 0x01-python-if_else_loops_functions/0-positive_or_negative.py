#!/usr/bin/python3

import random
numero = random.randint(-10, 10)
if numero > 0:
    print("{} is positive".format(numero))
elif numero == 0:
    print("{} is zero".format(numero))
else:
    print("{} is negative".format(numero))
