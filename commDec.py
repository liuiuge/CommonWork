'''
    some decorator
'''
from datetime import datetime
from functools import wraps

def tRecord(fn):
    @wraps(fn)
    def time_record(*args, **kwargs):
        t1 = datetime.now()
        result = fn(*args, **kwargs)
        t2 = datetime.now()
        print("@tRecord:" + fn.__name__, " took " + str(t2 - t1) + "")
        return result
    return time_record