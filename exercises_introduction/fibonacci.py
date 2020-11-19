def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        print(a, b = a + b)

print(fibonacci())