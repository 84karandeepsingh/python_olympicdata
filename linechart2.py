from pylab import *
 
year = [1956, 1960, 1964]
pop_luge = [0, 0, 5]
pop_skating = [0, 4, 3]
pop_skiing = [2, 5, 2]
plt.plot(year, pop_luge, color='green')
plt.plot(year, pop_skating, color='black')
plt.plot(year, pop_skiing, color='orange')
plt.xlabel('Years')
plt.ylabel('No. of medals')
plt.title('Medals won by sport')
plt.show()