def fibonacci():
    a, b = 0, 1
    while T:
        yield a
        a, b = b, a + b

# Sử dụng generator
fib_gen = fibonacci()
print(list(fib_gen))
for _ in range(10):
    print(next(fib_gen))

