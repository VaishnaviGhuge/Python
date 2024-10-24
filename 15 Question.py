#Print at even digit and at odd position alphabate of 6 digit
from random import *
for i in range(6):
    if i%2==0:
        print(chr(randint(65,65+25)),end="")
    else:
        print(randint(0,6),end="")
print()