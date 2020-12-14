import queue
import time
import threading
import bornPig


class MyThreadPool:
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self._pool = queue.Queue(maxsize)   # 使用queue队列，创建一个线程池
        for _ in range(maxsize):
            self._pool.put(threading.Thread)

    def get_thread(self):
        return self._pool.get()

    def add_thread(self):
        self._pool.put(threading.Thread)


def run(pool, arg):
    # print('执行任务', i)
    bornPig.smsSAR(arg)
    pool.add_thread()   # 执行完毕后，再向线程池中添加一个线程类


if __name__ == '__main__':
    invite = input('输入邀请码：')
    # invite = '8878Pf'
    # invite = '575JN4'
    # invite = '587ydT'
    # invite = '576reU'
    pool = MyThreadPool(10)  # 设定线程池中最多只能有10个线程类
    while True:
        t = pool.get_thread()   # 每个t都是一个线程类
        obj = t(target=run, args=(pool, invite))  # 这里的obj才是正真的线程对象
        obj.start()
    print("活动的子线程数： ", threading.active_count()-1)
