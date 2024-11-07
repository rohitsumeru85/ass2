 f = open ('test.txt', 'w')
  f.write('this is a test file')
  f.close()
  f = open ('test.txt', 'r')

  print(f.read())
  f.seek(4)
  print(f.readlines())
  import os
  print( os.path.getsize('test.txt'))
import io
with open('test.txt1','wb') as f:
  file = io.BufferedWriter(f)
  file.write(b'hello world \n')
  file.write(b'hello mr.rohit')
  file.flush()

print ('hello mr. rohit! how r u ? ')

import logging 
logging.basicConfig (filename = 'my.log', level = logging.INFO, format = '%(asctime)s %(message)s')
logging.info('log this line of execution')
logging.info('this is my logging infomation')
logging.critical('this is my logging and critical infomation')
logging.error('this is my logging and error infomation')
logging.warning('this is my logging and warning infomation')
logging.shutdown()

import threading 
import time
def first_thread(id):
  for i in range (10):
    print ('test1 %d printing %d' %(id,i))
    time.sleep(1)
first_thread(1)
thread1=[threading.Thread (target = first_thread, args = (i,)) for i in range (3)]
for t in thread1:
  t.start() 




import multiprocessing 
def my_process():
  print ('this is my multiprocessing programe')
if __name__ == '__main__' :
  m = multiprocessing.Process(target = my_process)
  print ('this is my main program')
  m.start()
  m.join()
  

  

  
