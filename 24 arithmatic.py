print("Statement-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("Statement-3")
print("Statement-4")
try:
    print(10/0)
except BaseException:
    print(11/2)
print("Statement-5")