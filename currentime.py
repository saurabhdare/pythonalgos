import time

ticks = time.time()

print("Number of ticks since 00:00 AM, January 1 1970:", ticks)
print('---------------------------------------------------------------')
print(time.localtime())
print('---------------------------------------------------------------')
print("Local current time: ",time.localtime(time.time()))
print('---------------------------------------------------------------')
print("Local formatted time: ", time.asctime(time.localtime(time.time())))
print('---------------------------------------------------------------')
