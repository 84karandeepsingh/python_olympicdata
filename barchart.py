import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 3
means_menwomen = (90, 55, 40)
means_silver = (85, 62, 54)
means_bronze = (55, 50, 40)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, means_menwomen, bar_width,
                 alpha=opacity,
                 color='b',
                 label='MenWomen')
 
rects2 = plt.bar(index + bar_width, means_silver, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Silver')
rects3 = plt.bar(index + bar_width, means_bronze, bar_width,
                 alpha=opacity,
                 color='y',
                 label='bronze'
plt.xlabel('Medals')
plt.ylabel('Number of medals')
plt.title('Medals won by men and women')
plt.xticks(index + bar_width, ('Gold', 'Silver', 'Bronze'))
plt.legend()
 
plt.tight_layout()
plt.show()
