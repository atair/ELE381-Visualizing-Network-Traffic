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
		buildingCounts[i] = sum(d.values())
		i += 1
	
	allBuildingCounts.append(buildingCounts)

np.save(os.path.join('Processed_Timestamp_Data', 'sundayBuildingData.npy'), allBuildingCounts)
    
