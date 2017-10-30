import queue
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import threading

pool = ThreadPoolExecutor(3)


def return_after_5_sec(msg="done"):
    sleep(3)
    print("waited 5 sec")
    return msg


def test_1():
    future = pool.submit(return_after_5_sec, "hello")
    print("submitted job")
    print("job done: {0}".format(future.done()))
    print("after done msg: {0}".format(future.result()))


def generator_func():
    for i in range(5):
        sleep(i/2)
        yield i


class SimpleGenerator:
    def __init__(self, maximum=1):
        self.max = maximum

    def __iter__(self):
        for i in range(self.max):
            sleep(i / 2)
            yield i


class SimpleGenerator2:
    def __init__(self, maximum=1):
        self.max = maximum
        self.cur = 0

    def __iter__(self):
        return self

    def next(self):
        sleep(2)
        self.cur += 1
        if self.cur < self.max:
            return self.cur
        else:
            raise StopIteration()


class IteratorGenerator:
    def __init__(self, maximum=1):
        self.max = maximum
        self.cur = 0

    def __iter__(self):
        for i in range(self.max):
            sleep(i / 2)
            yield i


def test_2():
    for x in generator_func():
        print(x)


def test_3():
    for x in SimpleGenerator(4):
        print(x)


def test_4():
    # this code
    sg = iter(IteratorGenerator(5))
    print(type(sg))
    print(sg.__next__())
    print(sg.__next__())
    print(sg.__next__())
    print(sg.__next__())
    print(sg.__next__())
    # is equivalent to:
    for x in IteratorGenerator(5):
        print(x)


def test_wait_for_thread():
    number_counter = threading.Thread(target=count_slowly, name="numbers", args=(10,))
    number_counter.start()
    number_counter.join()
    print("done")


def count_slowly(up_to):
    for x in range(up_to):
        print(x)
        sleep(0.5)


def print_words_slowly():
    for x in range(10):
        print("********")
        sleep(0.2)


def test_5():
    number_counter = threading.Thread(target=count_slowly, name="numbers", args=(25,))
    number_counter.start()
    words_counter = threading.Thread(target=print_words_slowly, name="words")
    words_counter.start()


def test_iterate_queue():
    q = queue.Queue()
    for i in range(5):
        q.put(i*2)
    try:
        for num in iter(q.get_nowait, None):
            print(str(num))
    except queue.Empty as e:
        print("empty")
    print("done")


def wait_for_one_thread():
    number_counter = threading.Thread(target=count_slowly, name="numbers", args=(15,))
    words_counter = threading.Thread(target=print_words_slowly, name="words")
    number_counter.start()
    words_counter.start()
    print("threads started")
    words_counter.join()
    print("words finished")
    number_counter.join()
    print("threads finished")


def my_print(value):
    str1 = str(value)
    print("got " + str1)
    sleep(2)
    print("after sleep " + str1)


def my_print2(obj):
    print("got " + obj["name"])
    sleep(2)
    print("after sleep " + obj["name"])


def pass_by_value():
    word = "start"
    print_thread = threading.Thread(target=my_print, name="numbers", args=(word,))
    print_thread.start()
    word = "end"
    print("word changed")
    print_thread.join()


def pass_by_reference():
    word = {"name": "gool"}
    my_print = threading.Thread(target=my_print2, name="numbers", args=(word,))
    my_print.start()
    word["name"] = "mool"
    my_print.join()

# run code
# test_1()
# test_2()
# test_3()
# test_4()
# test_5()
# test_iterate_queue()
# test_wait_for_thread()
# wait_for_one_thread()
# pass_by_reference()
# pass_by_value()

arr = [1,2,3,4,5]
del arr[:2]
print(arr)