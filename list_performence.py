import timeit
from array import array


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


def time_me_append():
    listush = bytearray()
    for i in range(1000000):
        listush.append(1)
    print(len(listush))


def time_me_assign():
    listush = bytearray()
    for i in range(1000000):
        listush += b'hello'
    print(len(listush))


def time_me_assign_2():
    listush = bytearray(1000000)
    for i in range(1000000):
        listush[i] = 1
    print(len(listush))


def time_me_extend():
    listush = bytearray()
    for i in range(1000000):
        listush.extend(b'hello')
    print(len(listush))

def del_1():
    listush = [None] * 1000000
    for i in range(100):
        del listush[i]


def del_2():
    listush = [None] * 1000000
    for i in range(1000000):
        tmp = listush[i]


class byte_fix:
    def __init__(self):
        self.start = 0
        self.end = 1

def add():
    video_bytes_queue = bytearray(10)
    print(len(video_bytes_queue))
    print(video_bytes_queue)
    for i in range(10):
        video_bytes_queue += bytearray(i)
    print(video_bytes_queue)


def add1():
    a = bytearray(b'LOTEM')
    b = bytearray(b'HIKI')
    for i in range(50_000_000):
        a += b
    print("end")


def add2():
    a = bytearray(b'LOTEM')
    b = bytearray(b'HIKI')
    for i in range(50_000_000):
    # while True:
        a.extend(b)
    print("end")

def add3():
    arr = array('b',[0] * 1_000_000)
    start = 0
    end = 1
    for i in range(100):

    arr.append(3)
    print(arr)





#
# print(timeit.timeit(stmt='time_me_append()',
#                         setup="from __main__ import time_me_append", number=1))
# print(timeit.timeit(stmt='time_me_assign()',
#                         setup="from __main__ import time_me_assign", number=1))
# print(timeit.timeit(stmt='time_me_assign_2()',
#                         setup="from __main__ import time_me_assign_2", number=1))
#
# print(timeit.timeit(stmt='time_me_extend()',
#                         setup="from __main__ import time_me_extend", number=1))

# print(timeit.timeit(stmt='del_1()',
#                         setup="from __main__ import del_1", number=1))
# print(timeit.timeit(stmt='del_2()',
#                         setup="from __main__ import del_2", number=1))

# add()

# print(timeit.timeit(stmt='add1()',
#                         setup="from __main__ import add1", number=1))
# print(timeit.timeit(stmt='add2()',
#                         setup="from __main__ import add2", number=1))
# add1()
add3()

