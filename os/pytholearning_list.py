import os

def main():
    try:
        path = os.getcwd()
        names = os.listdir(path)
        print(names)
        f = open('list_of_directory', 'w')
    except Exception:
        print('Check the rights in the file, please')
    else:
        for i in names:
            f.write(i + '\n')
        f.close()

    finally:
        print('The task has been solved')
if __name__ == '__main__':
    main()
