import numpy as np
from shapely.geometry import Polygon, Point
import folium
from folium import plugins
import random
import os
import pickle
from datetime import datetime, timedelta

from Raw_Timestamp_Data.saturdayTimestamps import timestamps

from Polyline_Bounding_Boxes.firestone import points as firestone_points
from Polyline_Bounding_Boxes.forbes import points as forbes_points
from Polyline_Bounding_Boxes.lewis import points as lewis_points
from Polyline_Bounding_Boxes.rockey_mathey import points as rockey_mathey_points
from Polyline_Bounding_Boxes.whitman import points as whitman_points
from Polyline_Bounding_Boxes.wilcox import points as wilcox_points
from Polyline_Bounding_Boxes.wu import points as wu_points


################################################################
# Load 24 hour data from saved file and generate dynamic heatmap
################################################################
with open ('outfileUpdated', 'rb') as fp:
	finalData = pickle.load(fp)

timeNames = []

for stamp in timestamps:
	unixUTCStamp = int(stamp[14:])
	estTimeStamp = datetime.utcfromtimestamp(unixUTCStamp) - timedelta(hours=4)
	timeNames.append(estTimeStamp.strftime('%I:%M %p'))

hm = plugins.HeatMapWithTime(finalData,index=timeNames,max_opacity=0.8, radius=5)
hm.add_to(m)

# Add Polylines:
for currBuilding in allBuildingPolygonPoints:
	correctedPoints = getPolyLine(currBuilding)
	folium.PolyLine(correctedPoints).add_to(m)
m.save('index3.html')