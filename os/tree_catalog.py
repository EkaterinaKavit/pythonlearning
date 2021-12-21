import os

def main():

    os.chdir('/home/galina/Desktop/pythonlearning/os/tree_catalog')
    path = os.getcwd()
    lots = list()
    for root, subdir, files in os.walk(path):
        #print(root)
        #print(subdir)
        #print(files)
        for file in files:
            if file[0] == 'M':
                lots.append(file[0:7])
        lots_unique = '\n'.join(set(lots))

    try:
        f = open('new_list_unique_lots.txt','w')
        f.write(lots_unique)
    except Exception as e:
        print(e)
    else:
        f.close()

if __name__ == '__main__':
    main()