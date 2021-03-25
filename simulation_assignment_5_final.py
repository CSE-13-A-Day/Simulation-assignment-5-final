# -*- coding: utf-8 -*-
"""Simulation_Assignment_5_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KHaZpmhVKTavji_iY7w0nyQdfFZAB_d-
"""

#Importing distribution method from scipy
from scipy.stats import *

#Declering list
customer = 20
interArrivalTime = []
arrivalTime = []
serviceTime = []
serviceTimeBegin = []
serviceTimeEnd = []
timeSpendSystem = []
timeIdleServer = []
waitingTime = []

#Generating random number by poisson distribution and assigining inter arrival time
mu = 5.6
for i in range (19):
  n = poisson.rvs(mu)
  interArrivalTime.append(n)

#Assigining first customer inter arrival time, arrival time, service time begin, waiting time, server idle time as zero
interArrivalTime.insert(0,0)
arrivalTime.insert(0,0)
serviceTimeBegin.insert(0,0)
waitingTime.insert(0,0)
timeIdleServer.insert(0,0)

#Calculatim arrival time from 2nd customer to 20th customer
for i in range (1,20):
    arrivalTime.append(interArrivalTime[i] + arrivalTime[i-1])

#For service time generating random number using exponential distribution
for i in range (20):
  n = expon.rvs(scale=5)
  serviceTime.append(round(n,2))

#Calculating service end time for first customer
serviceTimeEnd.insert(0,(serviceTime[0] + serviceTimeBegin[0]))

# Calculating service begins time and service end time for 2nd to 20th customers
for i in range (1,20):
  if (arrivalTime[i] > serviceTimeEnd[i-1]):
    serviceTimeBegin.insert(i,round(arrivalTime[i],2))
    serviceTimeEnd.insert(i,round((serviceTimeBegin[i] + serviceTime[i]),2))
  else:
    serviceTimeBegin.append(serviceTimeEnd[i-1])
    serviceTimeEnd.insert(i,round((serviceTimeBegin[i] + serviceTime[i]),2))

#Calculating waiting for customer 2nd to 20th
for i in range (1,20):
  if (serviceTimeBegin[i] > arrivalTime[i]):
    waitingTime.insert(i, round((serviceTimeBegin[i] - arrivalTime[i]),2))
  else:
    waitingTime.insert(i,0)

#Calculating time spend in system by the customes
for i in range(20):
  timeSpendSystem.insert(i, round((serviceTime[i] + waitingTime[i]),2))

#Calculating server idle time for customer 2nd to 20th
for i in range (1,20):
  if (serviceTimeEnd[i-1] < arrivalTime[i]):
    timeIdleServer.insert(i,round((arrivalTime[i] - serviceTimeEnd[i-1]),2))
  else:
    timeIdleServer.insert(i,0)

print("---------------------------------------------------------------------------------------------------------------------------------------------")
print("Customer\t Interarrival\t Arrival\t Service \t SBT\t\t SET\t\t Waiting \t Time Spend \t Server Idle")
print("   No\t \t     Time\t  Time\t\t  Time\t\t\t\t\t\t  Time\t\t in System\t    Time    ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
for i in range (1,21):
  print("   ",i ,"\t\t", interArrivalTime[i-1], "\t\t", arrivalTime[i-1], "\t\t", serviceTime[i-1], "\t\t", serviceTimeBegin[i-1], "\t\t" , serviceTimeEnd[i-1], "\t\t", waitingTime[i-1], "\t\t", timeSpendSystem[i-1], "\t\t", timeIdleServer[i-1])


sumInterArrival = sum(interArrivalTime)
sumService = round(sum(serviceTime),2)
sumWaiting = round(sum(waitingTime),2)
sumSpendSystem = round(sum(timeSpendSystem),2)
sumServerIdle = round(sum(timeIdleServer),2)

print("---------------------------------------------------------------------------------------------------------------------------------------------")
print("Total: \t","   TIAT=",sumInterArrival,"\t\t\t\tTST=",sumService,"\t\t\t\t\tTWT=",sumWaiting,"\t\tTTSIS=",sumSpendSystem,"\tTSIT",sumServerIdle)
print("---------------------------------------------------------------------------------------------------------------------------------------------")

avgWaitingTime = round(sumWaiting/customer,2)
print("Average Waiting Time: ",avgWaitingTime)
avgSpendSystemTime = round(sumSpendSystem/customer,2)
print("Average Time Spend in System: ",avgSpendSystemTime)
avgInterArrivalTime = round(sumInterArrival/(customer-1),2)
print("Average Time Between Arrival: ",avgInterArrivalTime)
avgServiceTime = round(sumService/customer,2)
print("Average Service Time: ",avgServiceTime)
proportionIdleServerTime = round(sumServerIdle/serviceTimeEnd[19],2)
print("The proportion of the idle time of the server: ",proportionIdleServerTime)