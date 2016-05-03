#decorator for function
import functools

def log1(func):
    def decorator(func):
        def wrapper(*args, **kw):
            print "hello wrold!"
            return func(*args, **kw)
        return wrapper
    return decorator


def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin is call %s' % text
            text(*args, **kw)
            print 'end is call %s' % text
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'hello_begin'
                res = func(*args, **kw)
                print 'hello_end'
                return res
            return wrapper
        return decorator

    
def log2():
    def decorator(func):
        @functools.wraps(func) 
        def wrapper(*args):
            print 'hello_begin'
            print 'call %s():' % func.__name__
            return func(*args)
            print 'hello_end'
        return wrapper
    return decorator


def log3():
    def decorator(func):
        print 'call_begin'
        return func()
        print 'call_end'
    return decorator
        
