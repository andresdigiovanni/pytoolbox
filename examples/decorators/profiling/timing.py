import time

from pytoolbox.decorators.profiling import timing


@timing
def sum(a, b):
    time.sleep(3)
    return a + b


if __name__ == "__main__":
    a, b = 3, 2
    sum(a, b)
