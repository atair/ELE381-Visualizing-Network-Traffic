import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import os

upDirectory = '.'
if os.name == 'nt':
	upDirectory = '..'
certDirectory = os.path.join(upDirectory, 'ele-381-course-project-firebase-adminsdk-n1b3y-2c948ee2ce.json')
cred = credentials.Certificate(certDirectory)
firebase_admin.initialize_app(cred)

db = firestore.client()

collectionName = u'2019-05-04'
docs = db.collection(collectionName).get()

# Get List of routers for building
routerList = {}
for doc in docs:
	d = doc.to_dict()
	for building in d.keys():	
		routerList[building] = list(d[building].keys())
	break

np.save("buildingToRouterDic.npy", routerList)

