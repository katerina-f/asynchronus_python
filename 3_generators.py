from time import time



def gen(s):
    for i in s:
        yield i

g = gen('kate')



def get_filename():
    i = 1
    while True:

        pattern = "file-{}.jpeg"
        t = int(time() * 1000)

        yield i
        yield pattern.format(str(t))

        i += 1


g = get_filename()
