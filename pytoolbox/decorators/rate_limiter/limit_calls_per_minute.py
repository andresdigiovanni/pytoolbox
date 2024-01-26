import time
from functools import wraps

last_call_times_all = {}


def limit_calls_per_minute(max_calls_per_minute):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Retrieve the list of last call times or create an empty list if not exists
            last_call_times = last_call_times_all.setdefault(func.__name__, [])

            # Record the current time for the current function call
            current_time = time.time()
            last_call_times.append(current_time)

            # Remove calls that occurred more than a minute ago
            last_call_times = [t for t in last_call_times if current_time - t <= 60]

            # Update the dictionary with the updated call times
            last_call_times_all[func.__name__] = last_call_times

            # Check if the calls per minute limit is exceeded
            if len(last_call_times) > max_calls_per_minute:
                # Calculate the necessary wait time
                time_to_wait = 60 - (current_time - last_call_times[0])
                if time_to_wait > 0:
                    print(time_to_wait)
                    time.sleep(time_to_wait)

            # Call the original function and return the result
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
