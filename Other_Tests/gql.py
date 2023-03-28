def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b
    print()

    # 巩固2：
    return a


m = int(input("Enter An Integer:"))
fib(m)


# # 巩固1：
# print(fib(10))



