#-*- coding = utf-8 -*-

import functools

def log(text):
    def decorator(func):
        print 'begin call'
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        print 'end call'
        return wrapper
    return decorator
