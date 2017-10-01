# In this we will see what happens if no exception handling is done

number1 = 100
number2 = 10

# Division by zero is being done
# encapsulating the doubtful code in try clause
try:
    quotient = number1/number2
    print("Quotient is {}".format(quotient))

    data = "Selftuts"
    #data.get('name')

    # defining an array
    myList=[1,2,3,4,5,6]
    print(myList[20])    

except ZeroDivisionError:
    print("Division by zero is being performed")
except AttributeError:
    print("Attribute Error Occured")
except IndexError:
    print("Index out of range error")

