import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import random
import itertools
import os
import sys
import copy

d = np.load('buildingToRouterDic.npy')
buildingToRouter = d.item()
buildings = list(buildingToRouter.keys())



upDirectory = '.'
if os.name == 'nt':
	upDirectory = '..'
certDirectory = os.path.join(upDirectory, 'ele-381-course-project-firebase-adminsdk-n1b3y-2c948ee2ce.json')
cred = credentials.Certificate(certDirectory)
firebase_admin.initialize_app(cred)

db = firestore.client()

collectionName = '2019-05-13_MAC'
docs = db.collection(collectionName).get()
prev = {}
curr = {}


k = 0
for doc in docs:
	print("Index: " + str(k))
	d = doc.to_dict()
	for i in range(len(buildings)):
		macAdresses = []
		for r in buildingToRouter[buildings[i]]:
			a = d.get(r)
			if a != None:
				for pair in a:
					macAdresses.append(list(pair.keys()))
			
		if i == 0 and k == 86:
			prev = set(list(itertools.chain.from_iterable(macAdresses)))
		elif i == 0 and k > 86:
			curr = set(list(itertools.chain.from_iterable(macAdresses)))
			prev = prev & curr
	k += 1

print(len(prev))
for i in prev:
	print(i)


