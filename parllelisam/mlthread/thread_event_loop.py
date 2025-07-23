import asyncio
import threading


# Function to run an event loop in a separate thread
def start_event_loop(name, delay):
    async def task():
        print(f"[{name}] Starting task")
        await asyncio.sleep(delay)
        print(f"[{name}] Task completed after {delay} seconds")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(task())
    loop.close()


# Create two threads, each with its own event loop
thread1 = threading.Thread(target=start_event_loop, args=("Loop-1", 2))
thread2 = threading.Thread(target=start_event_loop, args=("Loop-2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both event loops completed.")
