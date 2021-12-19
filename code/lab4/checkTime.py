import time
import taskOneWithCode
import taskTwoWithLibrary
import taskThereWithRegulars

print("Now testing my interpreter")
start_time = time.time()
for i in range(10):
    taskOneWithCode.convert()
print("--- %s seconds ---" % (time.time() - start_time))

print("Now testing some other library")
start_time = time.time()
for i in range(10):
    taskTwoWithLibrary.convert()
print("--- %s seconds ---" % (time.time() - start_time))

print("Now testing code with regulars")
start_time = time.time()
for i in range(10):
    taskThereWithRegulars.convert()
print("--- %s seconds ---" % (time.time() - start_time))
