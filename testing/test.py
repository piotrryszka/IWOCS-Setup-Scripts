import _thread
import time
import threading

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def print_star(delay):
    while 1:
        time.sleep(delay)
        print('*')

def counting_process(delay):
    while 1:
        time.sleep(delay)
        e = threading.active_count()
        print(e)



# Create threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
   _thread.start_new_thread(print_star, (0.5,))
   _thread.start_new_thread(counting_process, (2,))
   e = threading.active_count()
   print(e)

except:
   print ("Error: unable to start thread")


while 1:
   pass

# NEED TO FINISH THREADS AS WELL

