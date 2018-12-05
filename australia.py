import csv 

categories = []
australia = []
gender  = []

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
			gender.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals won by men:', len(australia))
print('total medals won by women:', len(australia))

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

# filter based on gender
#
# plot on a bar chart gender =>
# how many medals won by men by the percentage of medals won by women