from importlib import reload
import time
import test1
print("Function enetering into reload mode")
time.sleep(5)
reload(test1)
print("This is last line")