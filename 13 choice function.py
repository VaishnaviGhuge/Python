#choice function ==> choice()  it work for list,tuple doesnt support set only
from random import *
list=["sunny","bunny","chinny","vinny"]
for i in range(10):
    print(choice(list))