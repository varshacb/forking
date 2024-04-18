from multiprocessing import Process, Manager
import multiprocessing

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

def f1(d, l):
    d[1] = '2'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

def main():
    # with Manager() as manager:
        manager= multiprocessing.Manager()
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p1 = Process(target=f1,args=(d,l))
        p.start()
        # p1.start()
        p.join()
        # p1.join()

        print(d)
        print(l)


main()