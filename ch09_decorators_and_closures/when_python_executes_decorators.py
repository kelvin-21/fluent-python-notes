"""
Function decorators are executed as soon as the module is imported, but the decorated functions only run when they
are explicitly invoked
"""


registry = []
peek_results = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


def peek_result(func):
    print(f'running peek_result({func})')
    result = func()
    peek_results.append(result)
    return func


def try_except(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except:
            print('except...')
    return wrapper


@register
def f1():
    print('running f1()')
    return 1


@register
def f2():
    print('running f2()')
    return 2


@peek_result
def f3():
    print('running f3()')
    return 3


def main():
    print('running main()')
    print(f'registry -> {registry}')
    print(f'peek_results -> {peek_results}')
    # f1()
    # f2()
    # f3()


if __name__ == '__main__':
    main()
