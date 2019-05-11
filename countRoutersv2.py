import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import os
from datetime import datetime

day = 'thursday'
upDirectory = '.'
if os.name == 'nt':
	upDirectory = '..'

certDirectory = os.path.join(upDirectory, 'ele-381-course-project-firebase-adminsdk-n1b3y-2c948ee2ce.json')

buildingNames = []


def getRouters(timestamp, i):
	counts = []
	buildingNames = list(timestamp.keys())
	buildingNames.sort()


	for buildingName in buildingNames:
		counts.append(sum(timestamp[buildingName].values()))
	return counts

def formatTimeStamp(timestamp):
	time = timestamp[0:2]+':'+timestamp[2:4]
	d = datetime.strptime(time, "%H:%M")
	return d.strftime("%I:%M %p")

# Use a service account
cred = credentials.Certificate(certDirectory)
firebase_admin.initialize_app(cred)

db = firestore.client()

collectionName = u'2019-05-04'



# Building counts
firestoneCount = 0
forbesCount = 0
friendCount = 0
lewisCount = 0
rockyCount = 0
whitmanCount = 0
wuCount = 0
dillonCount = 0
fristCount = 0


buildingCounts  = [firestoneCount, forbesCount, friendCount, lewisCount, rockyCount, whitmanCount, wuCount, dillonCount, fristCount]


docs = db.collection(collectionName).get()
allBuildingCounts = []
timestamps = []
i = 0
for doc in docs:
	d = doc.to_dict()
	currCounts = getRouters(d, i)
	i += 1
	allBuildingCounts.append(currCounts)
	timestamps.append(formatTimeStamp(doc.id))

print(len(allBuildingCounts))
print(allBuildingCounts[0])
nparr = np.array(allBuildingCounts)
print(nparr.shape)
np.save(os.path.join('Processed_Timestamp_Data', day+'BuildingDataNEW.npy'), nparr)
np.save(os.path.join('Timestamp_names', day+'BuildingTimestampNames.npy'), np.array(timestamps))

