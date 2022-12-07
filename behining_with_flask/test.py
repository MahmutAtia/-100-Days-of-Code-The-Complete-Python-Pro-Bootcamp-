import time

current_time = time.time()


def speed_calc_decorator(function):
    def wrapper_func():
        current_time = time.time()
        function()
        time_after = time.time()
        print(time_after - current_time)
    return wrapper_func #dont forget not it


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i



def make_bold(func):
   def wrapper_func(*args):
        text =func(args[0])
        return "<b>"+text+"</b>"
   return wrapper_func

2