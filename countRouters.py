# Author: Abdulghafar Al Tair
# Get router values from buildings

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import os
from Raw_Timestamp_Data.sundayTimestamps import timestamps

upDirectory = '.'
if os.name == 'nt':
	upDirectory = '..'

certDirectory = os.path.join(upDirectory, 'ele-381-course-project-firebase-adminsdk-n1b3y-2c948ee2ce.json')


allBuildingCounts = []
# Use a service account
cred = credentials.Certificate(certDirectory)
firebase_admin.initialize_app(cred)

db = firestore.client()

def getRouters(building, i):
	count = 0
	for key, val in building.items():
		parts = key.split("-")
		if i == 0:
			count += val
		elif i == 1:
			count += val
		elif i == 2:
			if parts[0] == 'ap' and ((int(parts[2]) > 33 and int(parts[2]) < 44) or (int(parts[2]) > 49 and int(parts[2]) < 75)):
				count += val
		elif i == 3:
			count += val
		elif i == 4:
			if parts[0] == 'arun' and int(parts[1]) > 9128 and int(parts[1]) < 9145:
				count += val
		elif i == 5:
			if parts[0] == 'arun' and int(parts[1]) > 6982 and int(parts[1]) < 6991:
				count += val
		elif i == 6:
			if (parts[0] == 'ap' and (int(parts[2]) > 18 and int(parts[2]) < 26)) or \
			(parts[0] == "arun" and (int(parts[1]) > 6352 and int(parts[1]) < 6358)):
				count += val
	return count

# Reading Data
for t in timestamps:
	users_ref = db.collection(t)
	docs = users_ref.stream()

	# Building counts
	firestoneCount = 0
	forbesCount = 0
	friendCount = 0
	lewisCount = 0
	rockyCount = 0
	whitmanCount = 0
	wuCount = 0


	buildingCounts  = [firestoneCount, forbesCount, friendCount, lewisCount, rockyCount, whitmanCount, wuCount]


	i = 0
	for doc in docs:
		d = doc.to_dict()
		buildingCounts[i] = getRouters(d, i)
		i += 1
	
	allBuildingCounts.append(buildingCounts)

np.save(os.path.join('Processed_Timestamp_Data', 'sundayBuildingData.npy'), allBuildingCounts)
    
