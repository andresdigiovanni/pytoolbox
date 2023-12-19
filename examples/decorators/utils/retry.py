from pytoolbox.decorators.utils import retry

count = 0


@retry(max_tries=5, delay_seconds=1)
def great():
    global count
    count += 1

    if count < 5:
        raise Exception("Failed")

    print("Hello!")


if __name__ == "__main__":
    great()
