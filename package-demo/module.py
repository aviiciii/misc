
def say_hello(name=None):
    if not name:
        print('Hello, world!')
    else:
        print('Hello,' + name + '!')

def main():
    say_hello()
    say_hello('Python')

if __name__ == '__main__':
    main()