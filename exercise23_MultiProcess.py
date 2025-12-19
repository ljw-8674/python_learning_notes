"""
# Process--适合对进程生命周期、通信方式有精细控制的场景
from multiprocessing import Process
import os

def func(name):
    print(f'Running child process ({os.getpid()}) ...')

if __name__ == '__main__':
    print(f'Parent process ({os.getpid()}).')
    p = Process(target=func, args=('test',))
    print(f'Child process will start.')
    p.start()  # 启动进程
    p.join()   # 等待进程结束
    print(f'Child process end.')
"""
"""
# Pool--推荐用于并行任务
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print(f'Run task {name} ({os.getpid()})...')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'Task {name} runs {end - start:.2f} seconds.')

if __name__=='__main__':
    print(f'Parent process {os.getpid()}.')
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i + 1,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
"""
# 进程之间的通信
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print(f'Process to write: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'Put {value} to queue...')
        q.put(value)
        time.sleep(random.random())

def read(q):
    print(f'Process to read: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'Get {value} from queue.')

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
 
    pw.join()
    pr.terminate()
