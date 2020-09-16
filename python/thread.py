# 这个码运行的时候 main thread 已经开始了
import threading
import time

def func():
	print('ran')
	time.sleep(1)
	print("done")

# 这时候我们开了一个sub thread
x = threading.Thread(target = func)
x.start()

print("active thread: ", threading.activeCount()) # print the number of active thread

"""
$ python thread.py
ran
active thread: 2
done

"""
y = 0
COUNT = 10000

def adding2():
	global y
	for i in range(COUNT):
		y += 2

def adding3():
	global y
	for i in range(COUNT):
		y += 3

def subracting4():
	global y
	for i in range(COUNT):
		y -= 4

def subracting1():
	global y
	for i in range(COUNT):
		y -= 1

t2 = threading.Thread(target = adding2)
t3 = threading.Thread(target = adding3)
t4 = threading.Thread(target = subracting4)
t1 = threading.Thread(target = subracting1)

# 按理说 y 最后的值因该是 0 因为减了1000次加了一千次
# 但是当两个thread同时access变量y时，比如 0+3=3，0-1=-1 变量会随机被更新成3或-1

t2.start()
t3.start()
t4.start()
t1.start()

t2.join()
t3.join()
t4.join()
t1.join()

"""
without join:
+---+---+------------------                     main-thread
    |   |
    |   +...........                            child-thread(short)
    +..................................         child-thread(long)

with join
+---+---+------------------***********+###      main-thread
    |   |                             |
    |   +...........join()            |         child-thread(short)
    +......................join()......         child-thread(long)

with join and daemon thread
+-+--+---+------------------***********+###     parent-thread
  |  |   |                             |
  |  |   +...........join()            |        child-thread(short)
  |  +......................join()......        child-thread(long)
  +,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     child-thread(long + daemonized)

'-' main-thread/parent-thread/main-program execution
'.' child-thread execution
'#' optional parent-thread execution after join()-blocked parent-thread could 
    continue
'*' main-thread 'sleeping' in join-method, waiting for child-thread to finish
',' daemonized thread - 'ignores' lifetime of other threads;
    terminates when main-programs exits; is normally meant for 
    join-independent tasks
"""
print(y)


# ============================================================================

lock = threading.lock()

z = 0

def _adding2():
	global z
	with lock:
		for i in range(COUNT):
			z += 2

def _adding2():
	global z
	lock.acquire()
	for i in range(COUNT):
		z += 3
	lock.release()
	# with lock 是这两个function夹在一起的简写

_t2 = threading.Thread(target = _adding2)
_t3 = threading.Thread(target = _adding2)

# lock 完之后只有一个thread在某一时间点能access z

_t2.start()
_t3.start()

# 保证 z 最后为0

