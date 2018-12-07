from pylab import *
 
year = [1956, 1960, 1964]
pop_bronze = [1, 1, 3]
pop_gold = [1, 4, 3]
pop_silver = [0, 4, 4]
plt.plot(year, pop_bronze, color='brown')
plt.plot(year, pop_gold, color='yellow')
plt.plot(year, pop_silver, color='silver')
plt.xlabel('Years')
plt.ylabel('No. of medals')
plt.title('Medals won by categories')
plt.show()