import random
def lottery():
    for i in range(6):
        yield random.randint(1, 40)
    yield random.randint(1, 15)
for random_number in lottery():
    print("And the next number is... %d!" %(random_number))
def fibonaxi(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b
for i in fibonaxi(10):
    print(i)
def factorial(num):
    a, b = 1, 2
    for _ in range(num):
        yield a
        a, b = b, a * b
for i in factorial(10):
    print(i)