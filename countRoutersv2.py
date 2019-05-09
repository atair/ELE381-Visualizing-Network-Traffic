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

# buildingNames = [u'Friend-Center-0616', u'Whitman-College-0668', u'Madison-Hall-0036', u'Dillon-Gym-0067', u'Frist-Campus-Center-0605', u'Wu-Wilcox-0160', u'Forbes-College-Main-0148', u'Lewis-Library-0630', u'Firestone-0069']
buildingNames = []
# isFirst = 1

def getRouters(timestamp, i):
	counts = []
	# if isFirst:
	buildingNames = list(timestamp.keys())
	buildingNames.sort()
		# isFirst = 0

	for buildingName in buildingNames:
		counts.append(sum(timestamp[buildingName].values()))
	# for building, buildingData in timestamp.items():
	# 	counts.append(sum(buildingData.values()))
		# count += val
		# parts = key.split("-")
		# if i == 0:
		# 	count += val
		# elif i == 1:
		# 	count += val
		# elif i == 2:
		# 	if parts[0] == 'ap' and ((int(parts[2]) > 33 and int(parts[2]) < 44) or (int(parts[2]) > 49 and int(parts[2]) < 75)):
		# 		count += val
		# elif i == 3:
		# 	count += val
		# elif i == 4:
		# 	if parts[0] == 'arun' and int(parts[1]) > 9128 and int(parts[1]) < 9145:
		# 		count += val
		# elif i == 5:
		# 	if parts[0] == 'arun' and int(parts[1]) > 6982 and int(parts[1]) < 6991:
		# 		count += val
		# elif i == 6:
		# 	if (parts[0] == 'ap' and (int(parts[2]) > 18 and int(parts[2]) < 26)) or \
		# 	(parts[0] == "arun" and (int(parts[1]) > 6352 and int(parts[1]) < 6358)):
		# 		count += val
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

# users_ref = db.collection(collectionName)
# docs = users_ref.stream()

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