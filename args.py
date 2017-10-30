
def print_args(*args, **kwargs):
    print("unnamed arguments:")
    print(args)
    for index, value in enumerate(args):
        print('{0} - {1}'.format(index, value))

    print("kwargs = keyword arguments:")
    for name, value in kwargs.items():
        print('{0} - {1}'.format(name, value))

if __name__ == "__main__":
    print_args(233, "lotem", name="sharon", age=12)