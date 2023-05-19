# main.py
# Bank-Queue-Simulation
# CSCI 154

# The following program simulates a bank queue.

import heapq


# Window where customers are helped
window = [1,1,1,1,1,1,1,1,1,1]              # 1 means window is open, 0 means window is closed.
workRate = 10                               # Each window has a work rate of 10 units/hr

# Standard and Priority Customer Line
standardLine = []
priorityLine = []

class Customer:
    def __init__(self, ID, arrivalTime, work):
        self.ID = ID
        self.arrivalTime = arrivalTime
        self.work = work
    def setWaitTime(self, wait):                # question????? can wait be declared without a function
        self.wait= wait

# Need help to automate this
C1 = Customer()
C2 = Customer()
C3 = Customer()
C4 = Customer()
C5 = Customer()
customer = [C1, C2, C3, C4, C5]

class CustomerArrival:
    def __init__(self,)

eventList = []
