import csv 

categories = []
australia = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "AUS":
			australia.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for australia:', len(australia))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')
			

gold_2002 = []
gold_2006 =[]
gold_2010 = []

for medal in australia:
	if medal[0] == 2002 and medal[3] == "Gold":
					gold_2002.append(medal)

	if medal[0] == 2006 and medal[3] == "Gold":
					gold_2006.append(medal)	

	if medal[0] == 2010 and medal[3] == "Gold":
					gold_2010.append(medal)

print('australia won', len(gold_2002), 'gold medals in 2002')
print('australia won', len(gold_2006),  'gold medals in 2006')
print('australia won', len(gold_2010), 'gold medals in 2010')


print('processed', line_count, 'rows of data')

# filter 2010 based on years
#
# plot on a bar chart years =>
# how many medals for each year as  a percentage of the total