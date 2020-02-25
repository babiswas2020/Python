import asyncio
import random

async def task():
   print("Task started")
   await asyncio.sleep(random.randint(1,4))
   print("Task Completed")

async def task1():
   print("Task1 started")
   await asyncio.sleep(random.randint(1,4))
   print("Task1 Completed")

if __name__=="__main__":
  asyncio.run(task())
  asyncio.run(task1())

