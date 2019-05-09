import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

plt.rcParams.update({'font.size': 40})

day = 'thursday'

timeNames = list(np.load(os.path.join('Timestamp_names', day+'BuildingTimestampNames.npy')))
print(len(timeNames))
data = np.load(os.path.join('Processed_Timestamp_Data', day+'BuildingDataNEW.npy'))
print(data.shape)
# minVals = []
# for i in range(data.shape[1]):
# 	minVals.append(min(data[:,i]))

# minVals = np.array(minVals)
# data = data - minVals

names = ["Dillon-Gym", "Firestone", "Forbes-College-Main", "Friend-Center", "Frist-Campus-Center", "Lewis-Library", "Madison-Hall", "Whitman-College", "Wu-Wilcox"]

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
plt.ylabel('Total Router Connection Count')
plt.title('Thu. 5/4 12:15AM - Thu. 5/4 11:55PM')
plt.legend()
plt.show()
