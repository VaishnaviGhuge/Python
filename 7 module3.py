def f1():
    if __name__=="__main__":
        print("The code executed directly as a program")
        print("The value of __name__:", __name__)
    else:
        print("The code executeted indirectly as a module from some other program")
        print("The value of __name__ : ",__name__)
f1()