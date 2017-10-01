# This will raise an exception

try:
    print("Raising exception")
    raise ZeroDivisionError
    raise AttributeError

except ZeroDivisionError:

    print("Division by zero is being performed")

except AttributeError:

    print("Attribute error occured")
