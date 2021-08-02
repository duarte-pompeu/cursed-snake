import time
  
class TimerDecorator:
    
    def timeis(func):
        '''Decorator that reports the execution time.'''
        
        def wrap(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            
            print(func.__name__, end-start)
            return result
        return wrap
  
class Timer:
    @TimerDecorator.timeis
    def countdown(self, n):
        while n > 0:
            n -= 1

timer = Timer()
timer.countdown(10000)