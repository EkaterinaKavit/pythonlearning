try:
    f = open('try.txt')

except Exception:
    print('Error. Please check the name of the file.')

else:
    print(f.read())
    f.close()

finally:
    print('Блок работает всегда')