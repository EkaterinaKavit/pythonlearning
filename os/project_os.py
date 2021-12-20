import os

def main():

    path = os.getcwd()
    names = os.listdir(path)
    lots = []
    for name in names:
        if name[0]=='M':
            lots.append(name[0:7])
            lots_unique = '\n'.join(set(lots))

    try:
        f = open('unique_lots_new1.txt','w')
        f.write(lots_unique)
    except Exception:
        print('You have made en error')
    else:
        f.close()

if __name__ == '__main__':
    main()