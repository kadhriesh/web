import asyncio
import multiprocessing
import os

from leading_wildcard_test import main


# TARGET = 999900
#
#
# async def async_number_generator(shutdown_event):
#     for i in range(1, 10000000000):
#         if shutdown_event.is_set():
#             break
#         yield i
#
#
# async def read_data(shutdown_event):
#     async for number in async_number_generator(shutdown_event):
#         if shutdown_event.is_set():
#             break
#         if number == TARGET:
#             shutdown_event.set()
#             return number
#     return None


async def main_corutine(shutdown_event):
    # tasks = [asyncio.create_task(read_data(shutdown_event)) for _ in range(1, 10)]
    tasks = [asyncio.create_task(main(shutdown_event)) for _ in range(1, 5)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for data in done:
        result = await data
        print(f"Result: {result}")


def worker(shutdown_event):
    print("Worker started.")
    asyncio.run(main_corutine(shutdown_event))
    print("Worker end.")


if __name__ == "__main__":
    cpu_count = os.cpu_count()
    print(f"Total CPU cores: {cpu_count}")

    shutdown_event = multiprocessing.Event()
    processes = []
    for _ in range(cpu_count - 1):
        p = multiprocessing.Process(target=worker, args=(shutdown_event,))
        p.start()
        processes.append(p)

    shutdown_event.wait()
    for p in processes:
        p.terminate()
    for p in processes:
        p.join()
    print("Parent exiting.")
