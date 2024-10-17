def addition(x, y):
    return x + y

def division(x, y):
    if y == 0:
        raise ZeroDivisionError()
    return x / y