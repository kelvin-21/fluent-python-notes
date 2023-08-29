from ch09_decorators_and_closures.ad_hoc_runner.ad_hoc_task import AdHocTask


AD_HOC_TASKS = {}


def ad_hoc_task(obsolete_date: str):
    """Register function to ad hoc task"""
    def wrapper(func):
        new_task = AdHocTask(func.__name__, func, obsolete_date)
        AD_HOC_TASKS[func.__name__] = new_task
        print(f'Registered {new_task}')
    return wrapper


@ad_hoc_task(obsolete_date='2023-05-31')
def f1():
    ...


@ad_hoc_task(obsolete_date='2023-05-31')
def f2():
    ...


@ad_hoc_task(obsolete_date='2023-05-31')
def f3():
    ...


# @ad_hoc_task(obsolete_date='2023-05-')
def f4():
    ...
