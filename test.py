with open('test.txt', 'r') as a_file:

    lines = a_file.read()
    list_of_lists = lines.splitlines()

    a_file.close()

    print(list_of_lists)
    print(list_of_lists[0])