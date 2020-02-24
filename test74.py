import asyncio
import random

task=[]

async def task1():
   print("Task 1 started")
   await asyncio.sleep(random.randint(1,4))
   print("Task 1 completed")

async def task2():
   print("Task 2 started")
   await asyncio.sleep(random.randint(1,4))
   print("Task 2 completed")

async def task3():
   print("Task 3 started")
   await asyncio.sleep(random.randint(1,4))
   print("Task3 completed")

def add_task(task_def):
   global task
   task.append(task_def())

async def gather_task():
   await asyncio.gather(*task)


if __name__=="__main__":
   add_task(task1)
   add_task(task2)
   add_task(task3)
   loop=asyncio.get_event_loop()
   loop.run_until_complete(asyncio.ensure_future(gather_task()))
   loop.close()


