import os
import warnings
from contextlib import contextmanager, redirect_stderr, redirect_stdout


@contextmanager
def suppress_all_output():
    with open(os.devnull, "w") as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                yield (err, out)
