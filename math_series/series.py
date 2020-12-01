"""
The  Fibonacci Function
This Function is a sequence series of numbers where a number is the addition of the last two numbers, starting with 0, and 1.
"""

def fibonacci(n):
    if type(n) != int:
        return 'Plz Enter a Number'
    if n<0:
        return 'Plz Enter a positive Number'
    if n ==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(0))

"""
The  lucas Function
This lucas is a sequence series of numbers where a number is the addition of the last two numbers, starting with 2, and 1.
"""

def lucas(n):
    if type(n) != int:
        return 'Plz Enter a Number'
    if n<0:
        return 'Plz Enter a positive Number'
    if n ==0:
        return 2
    if n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

# print(lucas(0))

"""
The  Other_values Function
This Other_values is a sequence series of numbers where a number is the addition of the last two numbers, starting with values that provide by user.
"""

def other_values(n,first_value,second_value):
    if type(n) != int:
        return 'Plz Enter a Number'
    if n<0:
        return 'Plz Enter a positive Number'
    if n ==0:
        return first_value
    if n==1:
        return second_value
    else:
        return other_values(n-1,first_value,second_value)+other_values(n-2,first_value,second_value)

"""
The  sum_series Function
sum_series Function check the base value and cotrol the call of funtion to determin which function should run
"""

def sum_series(n,first_value=0,second_value=1):
    if first_value ==0 and second_value ==1:
        return fibonacci(n)
    elif first_value ==2 and second_value ==1:
        return lucas(n)
    else:
        return other_values(n,first_value,second_value)
    

print(sum_series(5,0,1))
print(sum_series(5,2,1))
print(sum_series(5,5,3))
print(sum_series(5))