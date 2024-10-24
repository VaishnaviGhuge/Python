#Write a program to generate 6 digit random number as OTP
from random import *
for i in range(6):
    print(randint(0,6),end="")