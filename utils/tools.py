import time


def time_to_timestamp(times=None):
    if times is None:
        times = time
    return int(times.time())
