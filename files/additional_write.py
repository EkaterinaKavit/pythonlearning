def main():
    try:
        f = open('file_for_test.txt','a')
        f.write('Добавим еще одно предложение\n')
        print('Record has been done.Congratulations.')
    except Exception as e:
        print(e)
    else:
        f.close()

if __name__ == '__main__':
    main()