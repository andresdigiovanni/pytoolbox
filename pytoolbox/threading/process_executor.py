import os
from concurrent.futures import ProcessPoolExecutor, as_completed


def process_executor(fn, input_data, *args, max_workers=None):
    """
    Example:
        def sum_3_nums(a, b, c):
            return a + b + c

        items = [(1, 2), (2, 3), (3, 4)]

        for x in process_executor(
            sum_3_nums,
            items,
            100
        ):
            print(x)
            # Output:
            # 103
            # 105
            # 107
    """

    if max_workers is None:
        max_workers = os.cpu_count()

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures_dict = {}
        for params in input_data:
            if isinstance(params, (list, tuple)):
                args_to_pass = params + args
            else:
                args_to_pass = (params,) + args

            future = executor.submit(fn, *args_to_pass)
            futures_dict[future] = params

        for future in as_completed(futures_dict):
            yield future.result()
