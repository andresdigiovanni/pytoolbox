import time
from functools import wraps

from tabulate import tabulate

execution_times = {}


def timing_profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        if func.__name__ in execution_times:
            execution_times[func.__name__].append(execution_time)
        else:
            execution_times[func.__name__] = [execution_time]

        return result

    return wrapper


def print_execution_times(reverse=False):
    table_data = []
    total_time = 0

    for func_name, times in execution_times.items():
        average_time = sum(times) / len(times)
        total_function_time = sum(times)
        table_data.append(
            [
                func_name,
                len(times),
                f"{average_time:.4f} seconds",
                f"{total_function_time:.4f} seconds",
            ]
        )
        total_time += total_function_time

    headers = ["Function", "Executions", "Average Time", "Total Time"]
    table_data.sort(key=lambda x: x[2], reverse=reverse)

    # Add a row for total time
    total_row = ["Total", "", "", f"{total_time:.4f} seconds"]
    table_data.append(total_row)

    print("\nExecution Time Summary:")
    print(tabulate(table_data, headers, tablefmt="grid"))
