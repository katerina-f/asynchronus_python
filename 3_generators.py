from time import time

def gen(s):
    for i in s:
        yield i

n = gen('kate')


def get_filename():
    i = 1
    while True:
        pattern = "file-{}.jpeg"
        t = int(time() * 1000)

        yield i
        yield pattern.format(str(t))

        i += 1

def gen(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen("kate")
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
