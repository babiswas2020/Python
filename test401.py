import schedule
import time

def job1():
   print("I am job1")

def job2():
   print("I am job2")

def job3():
   print("I am job3")

def job4():
   print("I am job4")

def job5():
   print("I am job 5")

def job6():
  print("I am job 6")

schedule.every(10).minutes.do(job1)
schedule.every().hour.do(job2)
schedule.every().day.at("00:00").do(job3)
schedule.every(5).to(10).minutes.do(job4)
schedule.every().monday.do(job5)
schedule.every().tuesday.at("18:00").do(job6)

while True:
   schedule.run_pending()
   time.sleep(1)

