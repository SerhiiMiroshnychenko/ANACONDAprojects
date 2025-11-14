x = 10

def increment_value():
    """Збільшує значення на одиницю."""
    global x
    x += 1
    print(f'{x = }')
    return x


b = increment_value()
print(f"x = {x}, b = {b}")
