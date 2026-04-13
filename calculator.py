def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error! Division by zero.'
    return x / y

def square_root(x):
    if x < 0:
        return 'Error! Negative input for square root.'
    return x ** 0.5

if __name__ == '__main__':
    print('Simple Calculator')
    print('Add:', add(5, 3))
    print('Subtract:', subtract(5, 3))
    print('Multiply:', multiply(5, 3))
    print('Divide:', divide(5, 0))  # Division by zero example
    print('Square Root:', square_root(9))