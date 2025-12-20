"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - ASYNC PROGRAMMING
═══════════════════════════════════════════════════════════════════════

Asynchronous programming with async/await.
Topics: coroutines, async/await, asyncio, async context managers
"""

import asyncio
import time

print("="*70)
print("ASYNC/AWAIT PROGRAMMING")
print("="*70)

# 1. ASYNC FUNCTION (COROUTINE)
print("--- Basic Async Function ---")

async def greet(name):
    """Async function returns coroutine"""
    print(f"Hello, {name}!")
    await asyncio.sleep(0.1)  # Async sleep
    return f"Greeted {name}"

# Run coroutine
# Python 3.7+: asyncio.run(greet("Alice"))
# Python 3.6: use get_event_loop()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(greet("Alice"))
print(f"Result: {result}")

# 2. RUNNING MULTIPLE TASKS
print("\n--- Concurrent Execution ---")

async def task(name, duration):
    print(f"{name} starting")
    await asyncio.sleep(duration)
    print(f"{name} done")
    return f"{name} result"

async def main():
    # Sequential (slow)
    start = time.time()
    await task("Task1", 0.1)
    await task("Task2", 0.1)
    print(f"Sequential: {time.time()-start:.2f}s")
    
    # Concurrent (fast!)
    start = time.time()
    results = await asyncio.gather(
        task("TaskA", 0.1),
        task("TaskB", 0.1),
        task("TaskC", 0.1)
    )
    print(f"Concurrent: {time.time()-start:.2f}s")
    print(f"Results: {results}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# 3. ASYNC WITH (CONTEXT MANAGER)
print("\n--- Async Context Manager ---")

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(0.1)

async def use_resource():
    async with AsyncResource() as resource:
        print("Using resource")

loop = asyncio.get_event_loop()
loop.run_until_complete(use_resource())

# 4. ASYNC ITERATOR
print("\n--- Async Iterator ---")

class AsyncCounter:
    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0.01)
        self.i += 1
        return self.i

async def iterate():
    async for num in AsyncCounter(5):
        print(num, end=" ")
    print()

loop = asyncio.get_event_loop()
loop.run_until_complete(iterate())

# 5. ASYNC GENERATOR
print("\n--- Async Generator ---")

async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.01)
        yield i

async def use_async_gen():
    async for num in async_range(5):
        print(num, end=" ")
    print()

loop = asyncio.get_event_loop()
loop.run_until_complete(use_async_gen())

# 6. TASK MANAGEMENT
print("\n--- Task Management ---")

async def background_task():
    while True:
        print("Background working...")
        await asyncio.sleep(0.2)
        # In real code, would have exit condition

async def main_with_tasks():
    # Create task (Python 3.7+: asyncio.create_task)
    # Python 3.6: use ensure_future
    task = asyncio.ensure_future(background_task())
    
    # Do other work
    await asyncio.sleep(0.5)
    
    # Cancel task
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Background task cancelled")

loop = asyncio.get_event_loop()
loop.run_until_complete(main_with_tasks())

# 7. PRACTICAL EXAMPLE
print("\n--- Practical: Async HTTP Requests ---")

async def fetch_data(url, delay):
    """Simulate fetching data from URL"""
    print(f"Fetching {url}")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def fetch_all():
    urls = [
        ("api.example.com/users", 0.1),
        ("api.example.com/posts", 0.15),
        ("api.example.com/comments", 0.12)
    ]
    
    tasks = [fetch_data(url, delay) for url, delay in urls]
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_all())

print("\n✓ async def creates coroutines")
print("✓ await pauses until async operation completes")
print("✓ asyncio.gather() runs tasks concurrently")
print("✓ Great for I/O-bound operations")
print("✓ Use async context managers with async with")
print("\nNote: Python 3.7+ can use asyncio.run()")
print("Python 3.6 uses: loop.run_until_complete()")

