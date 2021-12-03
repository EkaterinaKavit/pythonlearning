

class Fish:

    def __init__(self):
        print('Creation of the object')

def use_fish():
    pass

def use_delivery():
    print('Secret function use_delivery')

def main():

    use_fish()
    a = Fish()
    print('First Module name {}'.format(__name__))


if __name__ == '__main__':
    main()
