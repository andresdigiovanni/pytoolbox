import time
from functools import wraps


def retry(max_tries=3, delay_seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for tries in range(1, max_tries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {tries} failed: {e}")

                    if tries == max_tries:
                        print(
                            f"Function {func.__name__} failed after {max_tries} attempts"
                        )
                        raise e

                    time.sleep(delay_seconds)

        return wrapper

    return decorator
