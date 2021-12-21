def main():

    collection_list = [1,2,3,4]
    collection_list.append(4)
    #collection_list.append([10,11,12])
    collection_list.extend([5,8,9])
    collection_list.insert(0,52)
    print(collection_list)

    #сортировка
    #collection_list.sort()
    #print(collection_list)
    sorted_list = sorted(collection_list)
    print(sorted_list)

    # добавление нового элемента в set
    collection_set = {1,2,30}
    collection_set.add(85)
    print(collection_set)

    # сортировка
    sorted_set = sorted(collection_set)
    print(sorted_set)

    # добавление нового элемента в tuple

    collection_tuple = (10,20,30)
    # добавить новый элемент нельзя
    print(type(collection_tuple))
    sorted_tuple = sorted(collection_tuple)
    print(sorted_tuple)

    # добавление нового элемента в словарь

    collection_dictionary = {'name':'Jane','age':25}
    collection_dictionary['profession'] = 'doctor'
    collection_dictionary.update({'name':'Olga','age':34, 'profession':'veterinar'})
    print(collection_dictionary)

    # сортировка словаря
    dict_test = {'b':1, 'c':5, 'a':3}
    #sort by keys
    sorted_dictionary = sorted(dict_test.items(), key = lambda x:x[0])
    #sort by values
    sorted_dictionary = sorted(dict_test.items(), key=lambda x: x[1])
    print(sorted_dictionary)

if __name__ == '__main__':
    main()
