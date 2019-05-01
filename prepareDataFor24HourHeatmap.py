import numpy as np
from shapely.geometry import Polygon, Point
import folium
from folium import plugins
import random
import os
import pickle

from Polyline_Bounding_Boxes.firestone import points as firestone_points
from Polyline_Bounding_Boxes.forbes import points as forbes_points
from Polyline_Bounding_Boxes.lewis import points as lewis_points
from Polyline_Bounding_Boxes.rockey_mathey import points as rockey_mathey_points
from Polyline_Bounding_Boxes.whitman import points as whitman_points
from Polyline_Bounding_Boxes.wilcox import points as wilcox_points
from Polyline_Bounding_Boxes.wu import points as wu_points



def getPoints(buildingPoints, currBuildingCount, currBuildingPrevCount, currBuildingExistingPoints):
	correctedPoints = [(t[1], t[0]) for t in buildingPoints]
	poly = Polygon(correctedPoints)
	min_x, min_y, max_x, max_y = poly.bounds

	
	if currBuildingCount > currBuildingPrevCount: # Get more points
		numNewPoints = currBuildingCount - currBuildingPrevCount
		newLatitudes, newLongitudes = getExtraPoints(currBuildingExistingPoints, numNewPoints, min_x, min_y, max_x, max_y, poly)
		newPoints = [list(a) for a in zip(newLatitudes, newLongitudes)]
		for newPoint in newPoints:
			currBuildingExistingPoints.append(newPoint)

	else: # Remove Some Points
		numPointsToRemove = currBuildingPrevCount - currBuildingCount
		for i in range(numPointsToRemove):
			currBuildingExistingPoints.pop()
		# indcsPointstoRemove = random.sample(range(0, currBuildingPrevCount), numPointsToRemove)

	return currBuildingExistingPoints
def getExtraPoints(existingPoints, numExtraPoints, min_x, min_y, max_x, max_y, poly):
	points = []
	while len(points) < numExtraPoints:
		random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
		if random_point.within(poly) and doesNotExist(random_point, existingPoints):
			points.append(random_point)
	return getLatitudesAndLongitudes(points)

def doesNotExist(currPoint, existingPoints):
	return [currPoint.coords.xy[0][0], currPoint.coords.xy[1][0]] not in existingPoints

def getLatitudesAndLongitudes(points):
	latitudes = []
	longitudes = []

	for point in points:
		latitudes.append(point.coords.xy[0][0])
		longitudes.append(point.coords.xy[1][0])

	return latitudes, longitudes



allBuildingPolygonPoints = [firestone_points, forbes_points, lewis_points, rockey_mathey_points, whitman_points, wilcox_points, wu_points]


#############################################
# Generate data for 24 hours and save to file
#############################################
data = np.load(os.path.join('Processed_Timestamp_Data', 'saturdayBuildingData.npy'))
# Normalize the data
minVals = []
for i in range(data.shape[1]):
	minVals.append(min(data[:,i]))

minVals = np.array(minVals)
data = data - minVals

# variables
n = data.shape[0]
numOfBuildings = data.shape[1]

finalData = []
trackerOfAllPoints = [[]]*numOfBuildings


for i in range(n):
	#print("processing: " + str(i) + " out of " + str(n))
	currNumPoints = list(data[i,:])
	currDataPoints = []

	for currBuildingIndex in range(numOfBuildings):
		currBuildingPoints = allBuildingPolygonPoints[currBuildingIndex]
		currBuildingCount = currNumPoints[currBuildingIndex]

		if i == 0:
			currBuildingDataPoints = getPoints(currBuildingPoints, currBuildingCount, 0, trackerOfAllPoints[currBuildingIndex])
		else:
			currBuildingPrevCount = list(data[i-1,:])[currBuildingIndex]
			currBuildingDataPoints = getPoints(currBuildingPoints, currBuildingCount, currBuildingPrevCount, trackerOfAllPoints[currBuildingIndex])
		trackerOfAllPoints[currBuildingIndex] = currBuildingDataPoints
	
		currDataPoints.extend(currBuildingDataPoints)
	finalData.append(currDataPoints)


with open('outfileUpdated', 'wb') as fp:
	pickle.dump(finalData, fp)