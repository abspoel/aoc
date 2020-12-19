import sys
if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
    def input():
        return f.readline().strip()

def print_calls(func):
    def wrapper(*args):
        ret = func(*args)
        print(f"{func.__name__}{args} -> {ret}", file=sys.stderr)
        return ret
    return wrapper

def debug(*args, **kwargs):
    print(*args, file=sys.stderr)
