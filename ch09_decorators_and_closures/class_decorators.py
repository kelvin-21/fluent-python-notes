import time
import traceback
from functools import wraps


class Clock:
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = [repr(arg) for arg in args]
            arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
            arg_str = ', '.join(arg_lst)
            print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
            return result

        return wrapper


class TryExcept:
    def __init__(self, default_return=None):
        self.default_return = default_return

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as ex:
                print(f'[TryExcept] Error caught: {ex}\n{traceback.format_exc()}')
                return self.default_return
        return wrapper


@Clock()
def f1(a=0, b=1):
    time.sleep(a + b + 0.234)


@TryExcept(default_return=100)
def f2():
    raise NotImplementedError('sorry forgot')


if __name__ == '__main__':
    print(f2())
