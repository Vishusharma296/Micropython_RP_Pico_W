## ----- MicroPython Notes ------


### ------ Useful libraries and Modules for Micro Python ------

- machine
- os
- network
- time
- urequests
- ujson
- uio
- ubinascii
- math
- urandom
- _thread
- usyncio


#### ----------------- External libraries and modules ------------------

- umqtt
- BMP280, BME280
- 

### ------ Important Commands in CLI for Micropython -------


| Command                  | Description |
| -------------            | ------------- |
| help('modules')          | Gives the list of available/installed modules on Microcontroller |
| machine.unique_id()      | Retrieves the unique identifier of the microcontroller (MAC addr, hardware specific information)|


### -------------- Multi threading in Micro python ---------------

Using Multi threading in MicroPython, you can divide a program into smaller tasks that can run concurrently, such as handling user input, performing background calculations, or communicating with external devices. if done correctly, these threads run independently of each other and can perform tasks simultaneously without blocking.

#### Keywords and Terminology

- Event driven programming
- cooperative vs preemtive multitasking
- Coroutines, Lightweight threads
- Deadlocks
- Race conditions
- Asynchronous functions
- Locks
- Semaphores - semaphores can allow multiple threads to access a shared resource 
- Scheduling
- Concurrency Primitives
- Asynchronous I/O
- Queues
- Event flags
- Shared resources
- Design of concurrency model
- Scheduling


#### ------------- Functions and code snippets related to multi-threading -------------------



|  Functions                         | Description |
| -------------                      | ------------- |
| asyc def function_name():          | Asynchronous function for non blocking code |
| await uasyncio.sleep(time1)        | Non-blocking sleep, allows event scheduler to run something else |
| loop = uasyncio.get_event_loop()   | Creates an event loop |
| loop.create_task(function1())      | Can create and schedule multiple tasks for multiple functions f1, f2...|
| lock = _thread.allocate_lock()     | Create a lock object|
| lock.acquire()                     | | 
| lock.release()|| 



