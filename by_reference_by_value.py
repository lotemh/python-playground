
def my_print(string):
    print(string)


def pass_by_value():
    num_1 = 12
    print(num_1)
    num_2 = num_1
    num_1 = 100
    print(num_2)


def pass_by_reference():
    list_1 = [1,2,3]
    print("list 1 = {0}".format(list_1))
    list_2 = list_1
    print("assigned: list_2 = list_1")
    list_1.append(4)
    print("added 4 to list_1")
    print("list 1 = {0}".format(list_1))
    print("list_2 has changed as well. list 2 = {0}".format(list_2))
    print("assigned: list_1 = [100]")
    print("but now list_2 has not changed. list 2 = {0}".format(list_2))


def foo():

    list_1 = [1, 2]
    list_2 = list_1
    list_1 += [3, 4]
    print(list_2)

    arr_1 = bytearray([1,2,3])
    copy_of_arr_1 = arr_1
    arr_2 = bytearray([2,2])
    arr_1 += arr_1 + arr_2
    print(arr_1 == copy_of_arr_1)
    print(arr_1 is copy_of_arr_1)
    del arr_1[:1]
    print(arr_1 == copy_of_arr_1)



pass_by_reference()
pass_by_value()
foo()
