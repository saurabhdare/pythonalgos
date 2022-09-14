def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print("\t%s" % func.__name__, time.perf_counter() - t)
        return res
    return wrapper
