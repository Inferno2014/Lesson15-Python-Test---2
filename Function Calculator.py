def sum(n1, n2):
    return(n1 + n2)
def diff(n1, n2):
    if n1 > n2:
        return (n1 - n2)
    elif n1 < n2:
        return (n2 - n1)
def multiply(n1, n2):
    return(n1 * n2)
def div(n1, n2):
    if n1 > n2:
        return(n1 / n2)
    elif n1 < n2:
        return(n2 / n1)
try:
    n1 = int(input('Enter first number here: '))
    n2 = int(input('Enter second number here: '))
    calc = input('Enter choice of calculation(Addition, Subtraction, Multiplication or Division)here: ').lower()
except ValueError:
    print('Enter a valid value!')
if calc == 'addition':
    print("The sum is",sum(n1, n2))
elif calc == 'subtraction':
    print('The difference is',diff(n1, n2))
elif calc == 'multiplication':
    print('The product is',multiply(n1, n2))
try:
    if calc == 'division':
        print('The quotient is',div(n1, n2))
except ZeroDivisionError:
    print('Division by zero(0)is not possible!')


    