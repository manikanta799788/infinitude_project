def add(*args):
    return sum(args)

def sub(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
