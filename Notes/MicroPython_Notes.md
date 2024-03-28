## MicroPython Notes

### Useful libraries and Modules for Micro Python

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


#### External libraries and modules 

- umqtt
- bmp280
- 

<br>

### Important Commands in CLI for Micropython


| Command                  | Description |
| -------------            | ------------- |
| help('modules')          | Gives the list of available/installed modules on Microcontroller |
| machine.unique_id()      | Retrieves the unique identifier of the microcontroller (MAC addr, hardware specific information)|


### Concurrent programming in Micropython 

There are two main ways of doing concurrent programming in MPy: 1) Multi Threading, 2) Event Driven programming. These methods differ in their underlying mechanisms and how they handle concurrency. 

#### Multithreading

Multithreading involves executing multiple threads concurrently, where each thread represents a separate sequence of execution within the program. Threads can run in parallel on multicore processors or concurrently on single-core processors through time slicing. By using Multi threading in MicroPython, it is possible to divide a program into smaller tasks that can run concurrently. For example tasks such as handling user input, performing background calculations, or communicating with external devices. Another example of the use of multi-threading is when an IoT device needs to acquire sensor data and publish it to a server. These two tasks can run concurrently. If done correctly (with good concurrency design), these threads run independently of each other and perform tasks simultaneously without blocking. Multithreading enables true parallelism and can be beneficial for computationally intensive tasks or scenarios where true parallel execution is required.


#### Event driven programming

In event-driven programming, tasks are triggered by events or interrupts rather than being executed sequentially or concurrently. The program typically consists of an event loop that listens for events and dispatches tasks to handle them. Event-driven programming typically uses a single-threaded approach, where tasks are executed sequentially within the event loop. Tasks are executed cooperatively, with each task yielding control back to the event loop when waiting for I/O or other asynchronous operations. It is well-suited for applications that involve handling I/O-bound tasks or responding to external events quickly.


#### Keywords and Terminology for concurrent programming

- Event driven programming
- Multi-threading
- Cooperative vs preemptive multithreading
- Coroutines, Lightweight threads
- Deadlocks
- Race conditions
- Asynchronous functions
- Locks
- Semaphores 
- Scheduling
- Concurrency Primitives
- Asynchronous I/O
- Queues
- Event loops, Event flags, Event Handlers, Event Emitters
- Awaitable Objects
- Shared resources
- Callbacks
- Design of concurrency model

#### Functions and code snippets related to multithreading and event driven programming

|  Functions                         | Description |
| -------------                      | ------------- |
| asyc def function_name():          | Asynchronous function for non blocking code |
| await uasyncio.sleep(time1)        | Non-blocking sleep, allows event scheduler to run something else |
| loop = uasyncio.get_event_loop()   | Creates an event loop |
| loop.create_task(function1())      | Can create and schedule multiple tasks for multiple functions f1, f2...|
| lock = _thread.allocate_lock()     | Create a lock object|
| lock.acquire()                     | Method to acquire lock for threads | 
| lock.release()                     | Method to release lock for threads | 

### MQTT

For running MQTT client on RP picoW use the library [umqtt.simple](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple/umqtt)



