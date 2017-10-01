# In this we will see what happens if no exception handling is done

number1 = 100
number2 = 0

# defining the function
def performDivision():
    # Division by zero is being done
    # encapsulating the doubtful code in try clause
    try:
        quotient = number1/number2
        print("Quotient is {}".format(quotient))
    except FloatingPointError:
        print("Floating point error occurred")



try: 
    performDivision()
except ZeroDivisionError:
    print("Division by zero is being performed")



