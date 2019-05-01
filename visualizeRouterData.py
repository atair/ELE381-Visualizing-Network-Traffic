import numpy as np
import matplotlib.pyplot as plt
from Raw_Timestamp_Data.mondayTimestamps import timestamps
from datetime import datetime, timedelta
import os

plt.rcParams.update({'font.size': 40})

timeNames = []

for stamp in timestamps:
	unixUTCStamp = int(stamp[14:])
	estTimeStamp = datetime.utcfromtimestamp(unixUTCStamp) - timedelta(hours=4)
	timeNames.append(estTimeStamp.strftime('%I:%M %p'))
	

data = np.load(os.path.join('Processed_Timestamp_Data', 'mondayBuildingData.npy'))

names = ["Firestone Library", "Forbes", "Friend Center", "Lewis Library", "Rockey/Mathey Dhalls", "Whitman Dhall", "Wu/Wilcox Dhalls"]

f, ax = plt.subplots()
ax.tick_params(axis='x', which='both', labelsize=22)

l = list(range(1,len(timeNames)+1))

# for i in range(data.shape[1]):
for i in [0,2,3,4,5,6]:
	ax.plot(l, list(data[:,i]), label=names[i], linewidth=4)

newl = l[0::10]
ax.set_xticks(newl)
newlToIndices = [i-1 for i in newl]
xticks = [timeNames[i] for i in newlToIndices]
ax.set_xticklabels(xticks, rotation=70)

plt.xlabel('Time')
plt.ylabel('Total Router Connection Count')
plt.title('Mon. 4/29 6:00AM - Tue. 4/30 6:00AM')
plt.legend()
plt.show()
