import sys
import Queue

### Receive input
if len(sys.argv) == 2:
  inp = sys.argv[1]
else:
  print 'Error. Usage p8.py arg1'

### Initialize vars
q = Queue.Queue(13)
maxProduct = 0 
p = 1

### Find Max Product of 13 consecutive digits within input
for i in inp:
  if int(i) == 0:
    q.queue.clear()
    p = 1
  else:
    p *= int(i)
    if q.full():
      tmp = q.get()
      p /= tmp
      q.task_done()
      if p > maxProduct:
        maxProduct = p
    print i, p
    q.put(int(i))
print 'Max Product = ', maxProduct
