from multiprocessing.pool import Pool


# 简单的线程池多线程
def long_time_task(data, name):
    print('Run process      %s ----------> %s ' % (name, len(data)))
    for i in data:
        print("process %s    ----->  %s" % (name, i))

if __name__ == '__main__':
    ProcessNumber = 10  # 线程数量
    p = Pool(4)  # 线程池的数量
    numbers = list(range(846))

    # 线程平分任务
    pease = len(numbers) // ProcessNumber
    for i in range(ProcessNumber):
        p.apply_async(long_time_task, args=(numbers[i * pease: (i + 1) * pease], i))

    # 剩下的给最后一个进程
    if (not (len(numbers) % ProcessNumber) == 0):
        p.apply_async(long_time_task, args=(numbers[-(len(numbers) % ProcessNumber):], ProcessNumber + 1))

    p.close()
    p.join()
    print('任务完成~')
