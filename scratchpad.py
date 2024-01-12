# This is a sample Python script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def add_two(number):
    int_local = 2
    number = number + int_local
    print(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_list = ['Ann', 'Jill', 'Jane']
    last_list = ['Footill', 'Clayburn', 'Fonda']
    # create a list of (first, last) tuples
    temp_list = list(zip(first_list, last_list))
    print(temp_list)
    # convert the list to a dictionary
    names_dict = dict(temp_list)
    print(names_dict)

    # can you have a list inside a tuple?
    tl = ([1,2], ['a','b'])
    print(tl)
    print(type(tl))

    print(isinstance(3,int))

    print(sorted('cfda'))

