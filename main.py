from functools import wraps
from time import time

def timeit(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    start = time()
    result = f(*args, **kwargs)
    end = time()
    print(f'{f.__name__}({args}, {kwargs}) took {float(end-start)}s')
    return result
  return wrap

def main():
    @timeit
    def one_line():
        for _ in range(10000):
            lst = list([x for x in range(1000)])

    @timeit
    def normal_loop():
        for _ in range(10000):
            lst = list()
            for i in range(1000):
                lst.append(i)
    one_line()
    normal_loop()

if __name__ == '__main__':
    main()
