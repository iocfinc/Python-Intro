def spam(divideby):
    return 42 / divideby

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1)) # THIS WILL NOT GET EXECUTED unlike when it was inside a function.

except ZeroDivisionError:
    print("ERROR: INVALID ARGUMENT")
