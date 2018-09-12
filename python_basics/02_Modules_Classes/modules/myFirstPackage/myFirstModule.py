def f0():
    return f1() # f1 is in scope

def f1():
    return __name__

if __name__ == '__main__':
    print('I am running this as a script')


if __name__ == 'myFirstModule':
    print(' -----  I am running MyFirstModule.py as a module -----  ')

