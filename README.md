# Single-channel bank queueing system with python using distribution probability for 20 customers

# Introduction
Today banks are one of the most important units of the public. Most banks used standard
queuing models. It is very useful to avoid standing in a queue for a long time or in a wrong line
and to give tickets to all customers. Bank is an example of unlimited queue length.
Queuing is used to generate a sequence of customers' arrival time and to choose randomly
between three different services: open an account, transaction, and balance, with different period
of time for each service.

 A discrete event simulation on a single-server queuing system using the scipy library from python. The objective of running a simulation is to measure the performance of the system a priori and observe its behavior under predefined situations.
 
The elements of the system are simply the customers and the server and both can be persons or objects:
Customer: Receives the service
Server: Provides the service

![images](https://user-images.githubusercontent.com/41537584/112215261-5f57f300-8c4a-11eb-9488-c25180880d7d.png)

In this queuing system, one only server caters the arriving customers, which after being served leave the system. For the sake of simplicity we’ll assume that customers arrive at intervals following a poisson distribution, and the service time by the server also follow a exponential distribution.

Next arrival time is generated each time a customer arrives, meaning that when a customer arrives, we random sample inter-arrival time and compute the arrival time of the next customer. Similarly, when the customer goes to the server, we random sample the service time and compute the departure time of that customer. There will be times that customers arrive when there is still a customer being served, so they’d have to wait in the queue until the current customer departs and server is available. The flowchar below explains this in more details.

![image](https://user-images.githubusercontent.com/41537584/112214037-ee640b80-8c48-11eb-8550-c7f35a47ca8c.png)

# Equation
1. Average waiting time for a customer = Total time customer waiting in Queue/ Total number of customers						
2. The average time of a customer spend in system = total time spend in system/ total customer	
3. The average time between arrivals = sum of all time between arrivals / number of arrival-1				
4.  The average service time = total service time/ total number of customer									
5. The proportion of the idle time of the server = total idle time of server/total run time of simulation										

# Conclusion
To conclude, we built a simplistic queuing system with only one server, where arrival and service times follow a uniform distribution. In real life, obviously queuing systems are more complex as well as the probability distributions encountered. Nevertheless, this exercises is a good example of how once we have the code of a model built, it can be easily re-used to run experiments that can be useful to make decisions or foresee potential scenarios that might hinder the stability of the studied system

# Team Ratio
1. Md Farhan Nasir - (CSE-01306125)
2. Tashfia Haque - (CSE-01306144)
3. Farhadul Islam - (CSE-01306128)
4. S.M Mohiuddin - (CSE-01306094)

# Contact
1. farhannasir625@gmail.com
2. tashfiachy96@gmail.com
3. farhadmoonstar@gmail.com
4. mohiuddin.mohive@gmail.com


# Quick Link
1. https://pythonhosted.org/SimPy/Tutorials/TheBank.html
2. https://www.ijser.org/researchpaper/QUEUING-THEORY-APPLIED-IN-OUR-DAY-TO-DAY-LIFE.pdf

# Requirements
1. Google Colab/ Jupyter Notebook
2. Python 3.6
3. Scipy

# Result
![Output_1](https://user-images.githubusercontent.com/41537584/112633786-fea40280-8e63-11eb-9ad5-2054f4383d35.png)
![output_2](https://user-images.githubusercontent.com/41537584/112633806-0368b680-8e64-11eb-981a-ffad544a49b6.png)


