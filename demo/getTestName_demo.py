import inspect


def whoami():
    return inspect.stack()[1][3]


def my_func():
    x= whoami()
    print(x)


my_func()