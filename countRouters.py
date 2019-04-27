# Author: Abdulghafar Al Tair
# Get router values from buildings

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np

timestamps = [u'allRouterData_1556086818', u'allRouterData_1556087119', u'allRouterData_1556087419', u'allRouterData_1556087718', u'allRouterData_1556088018', u'allRouterData_1556088318', u'allRouterData_1556088619', u'allRouterData_1556088919', u'allRouterData_1556089218', u'allRouterData_1556092519', u'allRouterData_1556092818', u'allRouterData_1556093118', u'allRouterData_1556093420', u'allRouterData_1556093718', u'allRouterData_1556094017', u'allRouterData_1556094319', u'allRouterData_1556094619', u'allRouterData_1556094918', u'allRouterData_1556095218', u'allRouterData_1556098819', u'allRouterData_1556099120', u'allRouterData_1556099419', u'allRouterData_1556099720', u'allRouterData_1556100019', u'allRouterData_1556100318', u'allRouterData_1556100619', u'allRouterData_1556100919', u'allRouterData_1556101219', u'allRouterData_1556101518', u'allRouterData_1556102418', u'allRouterData_1556102719', u'allRouterData_1556103017', u'allRouterData_1556103320', u'allRouterData_1556103618', u'allRouterData_1556103919', u'allRouterData_1556104218', u'allRouterData_1556104519', u'allRouterData_1556104817', u'allRouterData_1556105117', u'allRouterData_1556109019', u'allRouterData_1556109318', u'allRouterData_1556109618', u'allRouterData_1556109919', u'allRouterData_1556110220', u'allRouterData_1556110519', u'allRouterData_1556110820', u'allRouterData_1556111118', u'allRouterData_1556111418', u'allRouterData_1556112618', u'allRouterData_1556112918', u'allRouterData_1556113219', u'allRouterData_1556113519', u'allRouterData_1556114119', u'allRouterData_1556114419', u'allRouterData_1556114718', u'allRouterData_1556115018', u'allRouterData_1556115319', u'allRouterData_1556116518', u'allRouterData_1556116818', u'allRouterData_1556117118', u'allRouterData_1556117420', u'allRouterData_1556117718', u'allRouterData_1556118019', u'allRouterData_1556118318', u'allRouterData_1556118619', u'allRouterData_1556118919', u'allRouterData_1556122518', u'allRouterData_1556122818', u'allRouterData_1556123119', u'allRouterData_1556123419', u'allRouterData_1556123719', u'allRouterData_1556124019', u'allRouterData_1556124318', u'allRouterData_1556124618', u'allRouterData_1556124919', u'allRouterData_1556125219', u'allRouterData_1556128820', u'allRouterData_1556129119', u'allRouterData_1556129418', u'allRouterData_1556129718', u'allRouterData_1556130018', u'allRouterData_1556130318', u'allRouterData_1556130620', u'allRouterData_1556130917', u'allRouterData_1556131220', u'allRouterData_1556131518', u'allRouterData_1556131818', u'allRouterData_1556135119', u'allRouterData_1556135419', u'allRouterData_1556135719', u'allRouterData_1556136019', u'allRouterData_1556136319', u'allRouterData_1556136618', u'allRouterData_1556136919', u'allRouterData_1556137219', u'allRouterData_1556137519', u'allRouterData_1556137819', u'allRouterData_1556138719', u'allRouterData_1556139019', u'allRouterData_1556139319', u'allRouterData_1556139618', u'allRouterData_1556139919', u'allRouterData_1556140218', u'allRouterData_1556140518', u'allRouterData_1556140821', u'allRouterData_1556141119', u'allRouterData_1556141418', u'allRouterData_1556142619', u'allRouterData_1556142918', u'allRouterData_1556143219', u'allRouterData_1556143518', u'allRouterData_1556143819', u'allRouterData_1556144119', u'allRouterData_1556144418', u'allRouterData_1556144719', u'allRouterData_1556145019', u'allRouterData_1556145318', u'allRouterData_1556146218', u'allRouterData_1556146519', u'allRouterData_1556146819', u'allRouterData_1556147119', u'allRouterData_1556147418', u'allRouterData_1556147719', u'allRouterData_1556148019', u'allRouterData_1556148318', u'allRouterData_1556148617', u'allRouterData_1556148919', u'allRouterData_1556152218', u'allRouterData_1556152519', u'allRouterData_1556152818', u'allRouterData_1556153175', u'allRouterData_1556153419', u'allRouterData_1556153718', u'allRouterData_1556154018', u'allRouterData_1556154319', u'allRouterData_1556154619', u'allRouterData_1556154919', u'allRouterData_1556155819', u'allRouterData_1556156118', u'allRouterData_1556156419', u'allRouterData_1556156719', u'allRouterData_1556157018', u'allRouterData_1556157318', u'allRouterData_1556157619', u'allRouterData_1556157919', u'allRouterData_1556158218', u'allRouterData_1556158519', u'allRouterData_1556159719', u'allRouterData_1556160018', u'allRouterData_1556160319', u'allRouterData_1556160618', u'allRouterData_1556160918', u'allRouterData_1556161219', u'allRouterData_1556161518', u'allRouterData_1556161818', u'allRouterData_1556162119', u'allRouterData_1556163319', u'allRouterData_1556163619', u'allRouterData_1556163918', u'allRouterData_1556164219', u'allRouterData_1556164519', u'allRouterData_1556164818', u'allRouterData_1556165120', u'allRouterData_1556165419', u'allRouterData_1556165720', u'allRouterData_1556166018', u'allRouterData_1556166619', u'allRouterData_1556166919', u'allRouterData_1556167218', u'allRouterData_1556167519', u'allRouterData_1556167818', u'allRouterData_1556168118', u'allRouterData_1556168421', u'allRouterData_1556168719', u'allRouterData_1556169017', u'allRouterData_1556169318', u'allRouterData_1556169618', u'allRouterData_1556173218']
allBuildingCounts = []
# Use a service account
cred = credentials.Certificate('./ele-381-course-project-firebase-adminsdk-n1b3y-2c948ee2ce.json')
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

np.save('weekdayBuildingData.npy', allBuildingCounts)
    
