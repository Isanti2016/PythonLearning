# -*- coding:utf-8 -*-

import random,time,queue
from multiprocessing.managers import BaseManager

task_queue=queue.Queue()
result_queue=queue.Queue()

class QueueManager(BaseManager):
    pass
#把两个queue都注册到网络上，callable参数关联queue对象
QueueManager.register('get_task_queue',callable=lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)
#绑定端口5000,设置验证码‘abc’
manager=QueueManager(address=('',5000),authkey=b'abc')
#启动queue:
manager.start()
#获得通过网络访问的queue对象
task=manager.get_task_queue()
result=manager.get_result_queue()
#放进去几个任务
for i in range(10):
    n=random.randint(0,1000)
    print('Put task %d...' % n)
    task.put(n)

#从result中读取结果
print("Try get result...")
for i in range(10):
    r=result.get(timeout=60)
    print('Result:%s' % r)

manager.shutdown()
print('master exit.')



