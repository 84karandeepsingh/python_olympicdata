import matplotlib.pyplot as plt
 
labels = ['Sapporo', 'Vancouver']
sizes = [91, 1]
colors = ['yellowgreen', 'lightcoral']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.title("Medal wins - Canada medals counts")
plt.tight_layout()
plt.xlabel("Medals won maximun and minimun in city")
plt.show()
