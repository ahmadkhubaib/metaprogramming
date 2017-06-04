from functools import wraps,partial
import logging

def debug(func=None, * ,prefix=''):

    if func is None:
        # print("None")
        return partial(debug, prefix=prefix)
    # log = logging.getLogger(func.__module__)
    msg = prefix + func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(log.debug(msg))
        print(msg)
        return func(*args, **kwargs)
    return wrapper


# to apply decorator on class level
def debugclass(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls

# to yank the attributes of class
def elementvalues(cls):
    orig_attribs = cls.__getattribute__

    def __getattribute__(self, name):
        print("Get : " + name)
        return orig_attribs(self,name)
    cls.__getattribute__ = __getattribute__
    return cls

