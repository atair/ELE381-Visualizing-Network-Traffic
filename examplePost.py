import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./ele-381-course-project-firebase-adminsdk-n1b3y-2c948ee2ce.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'Date').document(u'timeOfDay')
doc_ref.set({
    u'building_1': {
    u'router_a': 2,
    u'router_b': 3
    },
    u'building_2': {
    u'router_a': 5,
    u'router_b': 6
    }
})