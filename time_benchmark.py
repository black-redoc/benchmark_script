import time
from functools import partial, wraps


def __parametrized_benchmark__(dec):
    # enabled attributes setted in decorator
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@__parametrized_benchmark__
def time_benchmark(func, verbose=True):
    def wrapper():
        init = time.time()
        func()
        end = time.time()
        if verbose:
            print("\ttime elapsed: %.2f" % (end - init))

        return end - init

    return wrapper
