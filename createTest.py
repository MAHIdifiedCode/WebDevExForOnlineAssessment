import json
import random
candidateFirstName = input("Enter your first name: ") #1. get first name of candidate 
candidateLastName  = input("Enter your last name: ")  #1. get last name of candidate 
candidateEmailId   = input("Enter your e-mail Id: ")  #1. get candidate's email Id

#open and load session IDs database
f = open('sessDB.json',)
sessIDs = json.load(f)
candidateSessInfo=random.sample(sessIDs.items(), 1) #2. candidate gets unique session based on random selection
print(len(candidateSessInfo)) 
