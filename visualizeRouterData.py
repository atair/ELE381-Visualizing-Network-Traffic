import numpy as np
import matplotlib.pyplot as plt
from Raw_Timestamp_Data.sundayTimestamps import timestamps
from datetime import datetime, timedelta
import os

plt.rcParams.update({'font.size': 40})

timeNames = []

for stamp in timestamps:
	unixUTCStamp = int(stamp[14:])
	estTimeStamp = datetime.utcfromtimestamp(unixUTCStamp) - timedelta(hours=4)
	timeNames.append(estTimeStamp.strftime('%I:%M %p'))
	

data = np.load(os.path.join('Processed_Timestamp_Data', 'sundayBuildingData.npy'))

names = ["firestoneCount", "forbesCount", "friendCount", "lewisCount", "rockyCount", "whitmanCount", "wuCount"]

f, ax = plt.subplots()
ax.tick_params(axis='x', which='both', labelsize=22)

l = list(range(1,len(timeNames)+1))

for i in range(data.shape[1]):
	ax.plot(l, list(data[:,i]), label=names[i], linewidth=4)

newl = l[0::10]
ax.set_xticks(newl)
newlToIndices = [i-1 for i in newl]
xticks = [timeNames[i] for i in newlToIndices]
ax.set_xticklabels(xticks, rotation=70)

plt.xlabel('Time')
plt.ylabel('Total Counts')
plt.title('Sun. 4/28 5:30AM - Mon. 4/29 6:00AM')
plt.legend()
plt.show()
