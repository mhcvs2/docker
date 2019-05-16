import time


def t1():
    s = "mhc log test for {}\n"
    i = 0

    while True:
        with open("/tmp/t1.log", "a") as f:
            try:
                ss = s.format(str(i))
                print(ss)
                f.write(ss)
                i += 1
                time.sleep(2)
            except KeyboardInterrupt as e:
                break


def t2():
    s = "55.3.244.1 GET /index.html 15824 0.043"
    with open("/tmp/t1.log", "a") as f:
        ss = "{}\n".format(s)
        print(ss)
        f.write(ss)


if __name__ == '__main__':
    t2()

