import time


def time_it(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Start: ", func, args, kwargs)
        result = func(*args, **kwargs)
        using = (time.time() - now) * 1000
        using /= 1000
        using /= 60
        print("End: ", func, using, args, kwargs)
        return result

    return wrapper
