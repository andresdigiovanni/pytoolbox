from pytoolbox.decorators.utils import repeat


@repeat(5)
def great():
    print("Hello!")


if __name__ == "__main__":
    great()
