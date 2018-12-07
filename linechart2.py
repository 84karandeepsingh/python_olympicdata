from pylab import *
 
name = [luge, Skating, Skiing]
pop_bronze = [1, 2, 2]
pop_gold = [0, 2, 5]
pop_silver = [4, 4, 1]
plt.plot(year, pop_bronze, color='brown')
plt.plot(year, pop_gold, color='yellow')
plt.plot(year, pop_silver, color='silver')
plt.xlabel('name')
plt.ylabel('No. of medals')
plt.title('Medals won by categories')
plt.show()