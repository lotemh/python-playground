import timeit


def foo():
    print("foo")
    print("assignment =")
    arr_1 = bytearray([1, 2, 3])
    copy_of_arr_1 = arr_1
    arr_2 = bytearray([1, 2, 3])
    print("arr_1 == copy_of_arr_1: ", arr_1 == copy_of_arr_1)
    print("arr_1 is copy_of_arr_1: ", arr_1 is copy_of_arr_1)
    print("arr_1 == arr_2: ", arr_1 == arr_2)
    print("arr_1 is arr_2: ", arr_1 is arr_2)

    print("assignment +=")
    list_1 = [1, 2]
    list_2 = list_1
    list_1 += [3, 4]
    print("list 2: ", list_2)

    print("delete del arr[2]")
    arr_1 += arr_1 + arr_2
    del arr_1[:1]
    print("arr_1 is copy_of_arr_1: ", arr_1 is copy_of_arr_1)


def print_me():
    print("printing")


foo()
print(timeit.timeit(stmt='time_me()',
                        setup="from __main__ import time_me", number=2))
