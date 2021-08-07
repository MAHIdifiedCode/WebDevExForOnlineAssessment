import json
import random
import time as t
import os
from multiprocessing import Process
from threading import Thread

candidateFirstName = input("Enter your first name: ") #1. get first name of candidate 
candidateLastName  = input("Enter your last name: ")  #1. get last name of candidate 
candidateEmailId   = input("Enter your e-mail Id: ")  #1. get candidate's email Id

f = open('sessDB.json',) #open and load session IDs database
sessIDs = json.load(f)
f.close()
candidateSessInfo=random.sample(sessIDs.items(), 1) #2. candidate gets unique session based on random selection from session database {Ex. session Id, _desc:dsaQPx}. It determines the set of questions he is asked.
print(candidateSessInfo)
candidateQPTypeInfo = [item[1] for item in candidateSessInfo] #question paper type is a set of these questions. _desc:dsaQPx
print(candidateQPTypeInfo)
QPTypeAssigned = candidateQPTypeInfo[0] 

f = open('qpDB.json',) #open and get question papers from QP database
QP = json.load(f)
f.close()
for qp in QP:
    print(qp)


print("You have one hour to complete the assessment.")
candidateStartsResp = input("\nPress Enter when ready.")
print("Your time starts now!")

def loopA():
#implements timer in python
    time = 3600
    os.system("clear")
    while(time > 0):
          mint = int(time / 60)
          hrs = int((mint/60))
          sec = time % 60
          print("time left --> {}:{}:{}".format(hrs,mint,sec), end = "\r")
          time-=1
          t.sleep(1)

 
    # os.system('clear')
# else:
   # print("Your time is up!")

def loopB():
        print("Your time is not up!")  
        input("Select Yes!")

if __name__ == '__main__':
    Thread(target=loopB).start()
    Thread(target=loopA).start()
    