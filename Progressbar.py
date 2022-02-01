from tqdm.notebook import tqdm_notebook
import time
import numpy as np

#input dates
import datetime
#start Date Of Campaign 
d1=input("Enter start date: ? (in DD/MM/YYYY) ")
D1=datetime.datetime.strptime(d1,"%d/%m/%Y").date()
print("Your start date : "+D1.strftime('%d/%B/%Y')) 

#End Date Of Campaign 
d2=input("Enter end date: ? (in DD/MM/YYYY) ")
D2=datetime.datetime.strptime(d2,"%d/%m/%Y").date()
print("Your end date : "+D2.strftime('%d/%B/%Y')) 
#Campaign Running Days
datediff = abs((D2-D1).days)
print("Number of days Campaign Run",datediff)

#Prob Of addspot From All Adspot

#list Of Addspot
lst1 = []
lst1 = [int(item) for item in input("Enter All Adspots : ").split()]

#length List
length = len(lst1)
print(length)

#Addspot Input
k = int(input("Enter Which Adspot You Want to Know : "))
count = lst1.count(k)

#RoundOff 
p = int((count / length)*100)
print("Prob of Addspot from all adspot",p)

#List From Which We Have To Select Total Size Of Campaign
lst2 = []
lst2 = [int(item) for item in input("Enter Total Size of Campaign  : ").split()]
print(sum(lst2))

n = int((p*(datediff)) / sum(lst2))

print("Overall Percentage",n)


# loop for Pacing Probability Displayed by n
if n > 0 and n <= 24 :print("Red And Alert")
if n >= 25 and n <= 84:print("yellow")
if n >= 85 and n <= 100:print("green")
for i in tqdm_notebook(range(100)):
    if n == i:
        print(i)
        break
    time.sleep(0.1)
