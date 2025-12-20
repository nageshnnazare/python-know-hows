"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - CONCURRENCY
═══════════════════════════════════════════════════════════════════════

Threading and multiprocessing for parallel execution.
Topics: threading, multiprocessing, GIL, locks, queues
"""

import threading
import multiprocessing
import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

print("="*70)
print("CONCURRENCY - Threading & Multiprocessing")
print("="*70)

# 1. THREADING BASICS
print("--- Basic Threading ---")

def worker(name, duration):
    print(f"{name} starting")
    time.sleep(duration)
    print(f"{name} done")

# Create threads
t1 = threading.Thread(target=worker, args=("Thread-1", 0.1))
t2 = threading.Thread(target=worker, args=("Thread-2", 0.1))

# Start threads
start = time.time()
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()
print(f"Total time: {time.time()-start:.2f}s")

# 2. THREAD-SAFE QUEUE
print("\n--- Thread-Safe Queue ---")

def producer(queue, n):
    for i in range(n):
        queue.put(i)
        print(f"Produced: {i}")
        time.sleep(0.05)
    queue.put(None)  # Sentinel

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(0.1)

q = Queue()
prod_thread = threading.Thread(target=producer, args=(q, 5))
cons_thread = threading.Thread(target=consumer, args=(q,))

prod_thread.start()
cons_thread.start()
prod_thread.join()
cons_thread.join()

# 3. LOCKS FOR SYNCHRONIZATION
print("\n--- Thread Locks ---")

counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:  # Acquire lock
            counter += 1

threads = [threading.Thread(target=increment, args=(1000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter: {counter}")

# 4. THREAD POOL EXECUTOR
print("\n--- Thread Pool ---")

def task(n):
    time.sleep(0.1)
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    results = [f.result() for f in futures]
    print(f"Results: {results}")

# 5. MULTIPROCESSING BASICS
print("\n--- Multiprocessing ---")

def cpu_task(n):
    """CPU-intensive task"""
    return sum(i*i for i in range(n))

# Sequential
start = time.time()
results = [cpu_task(100000) for _ in range(4)]
print(f"Sequential: {time.time()-start:.2f}s")

# Parallel (if enough cores)
start = time.time()
with ProcessPoolExecutor() as executor:
    results = list(executor.map(cpu_task, [100000]*4))
print(f"Parallel: {time.time()-start:.2f}s")

# 6. PROCESS COMMUNICATION
print("\n--- Process Queue ---")

def worker_process(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        result = item * 2
        print(f"Process {multiprocessing.current_process().name}: {item} -> {result}")

# Note: This works best when run as main script
print("(Process queue example - works best as main script)")

# 7. WHEN TO USE WHAT
print("\n--- Threading vs Multiprocessing ---")

print("""
Threading:
  ✓ I/O-bound tasks (network, file operations)
  ✓ Shared memory (easy data sharing)
  ✗ GIL limits CPU-bound parallelism
  
Multiprocessing:
  ✓ CPU-bound tasks (computations)
  ✓ True parallelism (no GIL)
  ✗ More overhead
  ✗ Data copying between processes
  
Async/Await:
  ✓ I/O-bound with many concurrent operations
  ✓ Single-threaded efficiency
  ✓ Great for network programming
""")

# 8. PRACTICAL PATTERNS
print("--- Practical Patterns ---")

def download_file(url):
    """Simulate file download"""
    print(f"Downloading {url}")
    time.sleep(0.1)
    return f"Content from {url}"

urls = [f"url-{i}" for i in range(5)]

# Using thread pool for I/O-bound
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download_file, urls)
    print(f"Downloaded {len(list(results))} files")

print("\n✓ Use threading for I/O-bound tasks")
print("✓ Use multiprocessing for CPU-bound tasks")
print("✓ Use locks to protect shared data")
print("✓ Thread/Process pools manage resources")
print("✓ GIL limits Python thread parallelism")

