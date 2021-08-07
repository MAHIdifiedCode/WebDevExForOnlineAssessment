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
candidateQPTypeInfo = [item[1] for item in candidateSessInfo] #question paper type is a set of these questions. _desc:dsaQPx
QPTypeAssigned = candidateQPTypeInfo[0] 
f = open('qpDB.json',) #open and get question papers from QP database
QP = json.load(f)
f.close()
for qp in QP:
    if (qp == QPTypeAssigned["_desc"]):
       QPForCand =  QP[qp]
       
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

def loopB():
            allQuestionsList = QPForCand["Qset"]
            cnt = 0 #counter to store answers of questions
            #arrays to store question number and corresponding candidate response
            qNum = []
            ans =  []
            for q in allQuestionsList:
                qNum.append(q.keys())
                print (q) #3. candidate gets questions one by one on the screen and waits for candidate response for each que.
                ans.append(input ("Enter your choice!\n")) #4. candidate responses are submitted and stored in json format
            listToStrqNum = ' '.join([str(elem) for elem in qNum]) #converting list to string to store in json format
            candidateResponses = {'candidate Info':[{'First Name': candidateFirstName,'Last Name': candidateLastName, 'email ID': candidateEmailId, 'Que': listToStrqNum, 'Ans': ans}]}
            with open ('data.json', 'w') as f: 
                 json.dump(candidateResponses, f)
            f.close()
            print ("Thanks for completing your assessment. Your responses were stored!") #. Gets a confirmation of submitted assessment

if __name__ == '__main__':
    Thread(target=loopB).start()
    Thread(target=loopA).start()
    