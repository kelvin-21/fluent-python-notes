from ch09_decorators_and_closures.ad_hoc_runner.ad_hoc_task import AdHocTask


AD_HOC_TASKS = {}


def register_ad_hoc_task(obsolete_date: str):
    def wrapper(func):
        new_task = AdHocTask(func.__name__, func, obsolete_date)
        AD_HOC_TASKS[func.__name__] = new_task
        print(f'Registered {new_task}')
    return wrapper
