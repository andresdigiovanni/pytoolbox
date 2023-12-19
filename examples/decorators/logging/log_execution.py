from pytoolbox.decorators.logging import log_execution


@log_execution
def sum(a, b):
    return a + b


if __name__ == "__main__":
    a, b = 3, 2
    sum(a, b)
