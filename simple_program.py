def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    print(greet("World"))
    print(f"3 + 4 = {add(3, 4)}")
    for n in range(1, 6):
        status = "even" if is_even(n) else "odd"
        print(f"{n} is {status}")
