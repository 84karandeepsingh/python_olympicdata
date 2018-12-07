import csv 

categories = []
eua = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "EUA":
			eua.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for eua:', len(eua))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')
			

silver_1960 = []
silver_1964 = []

for medal in eua:
	if medal[0] == 1960 and medal[3] == "Silver":
					silver_1960.append(medal)

	if medal[0] == 1964 and medal[3] == "Silver":
					silver_1964.append(medal)	

print('eua won', len(silver_1960), 'silver medals in 1960')
print('eua won', len(silver_1964),  'silver medals in 1964')



print('processed', line_count, 'rows of data')

# filter 2010 based on years
#
# plot on a bar chart years =>
# how many medals for each year as  a percentage of the total
