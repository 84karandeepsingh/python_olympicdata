import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 6
means_men = (4, 0, 1, 1, 1, 1)
means_women = (0, 1, 1, 1, 2, 2)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Men')
 
rects2 = plt.bar(index + bar_width, means_women, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Women')
 
plt.xlabel('Years')
plt.ylabel('No. of medals')
plt.title('Medals won by Men and Women')
plt.xticks(index + bar_width, ('1994', '1998', '2002', '2006', '2010', '2014'))
plt.legend()
 
plt.tight_layout()
plt.show()