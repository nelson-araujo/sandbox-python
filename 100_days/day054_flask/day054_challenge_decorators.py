import time

def main():
    func01_run_time = func01()

    func02_run_time = func02()
    
    func03_run_time = func03()

    print(f'\nfunction\truntime (seconds)')
    print(f'--------\t-----------------')
    print(f'func01  \t{func01_run_time} seconds')
    print(f'func02  \t{func02_run_time} seconds')
    print(f'func03  \t{func03_run_time} seconds')

def func_speed_decorator(function):

    def wrapper():
        print(f'Testing {function.__name__}')
        
        start_time = time.time()
        # print(f'start: {start_time}')

        # print(f'running...')
        function()
        
        end_time= time.time()
        # print(f'end: {end_time}')

        run_time = end_time - start_time
        # print(f'runtime: {run_time} seconds\n')

        return run_time

    return wrapper

@func_speed_decorator
def func01():
    for i in range(10000000):
        i+i

@func_speed_decorator
def func02():
    for i in range(50000000):
        i+i

@func_speed_decorator
def func03():
    for i in range(100000000):
        i+i


# Redirect app entry point
if __name__ == '__main__':
    main()