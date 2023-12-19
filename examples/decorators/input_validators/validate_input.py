from pytoolbox.decorators.input_validators import validate_input


@validate_input(lambda x: isinstance(x, int), lambda x: isinstance(x, int))
def sum(a, b):
    return a + b


if __name__ == "__main__":
    a, b = 3, 2
    result = sum(a, b)
    print(f"{a} + {b} = {result}")
