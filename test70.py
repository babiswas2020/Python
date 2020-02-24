import asyncio
import random

task=[]

async def task1():
   print("task1 started")
   await asyncio.sleep(random.randint(1,4))
   print("task1 completed")


async def task2():
   print("task2 started")
   await asyncio.sleep(random.randint(1,4))
   print("task2 completed")


async def task3():
   print("task3 started")
   await asyncio.sleep(random.randint(1,4))
   print("task3 completed")

def add_task(task_def):
    global task
    task.append(task_def())

async def main():
   await asyncio.gather(*task)


if __name__=="__main__":
   add_task(task1)
   add_task(task2)
   add_task(task3)
   loop=asyncio.get_event_loop()
   loop.run_until_complete(asyncio.ensure_future(main()))
   loop.close()






