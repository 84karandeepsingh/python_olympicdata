import csv 

categories = []
austria = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "AUT":
			austria.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for austria:', len(austria))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')
			

silver_1928 = []
silver_1936 = []
silver_2014 = []

for medal in austria:
	if medal[0] == 1928 and medal[3] == "Silver":
					silver_1928.append(medal)

	if medal[0] == 1936 and medal[3] == "Silver":
					silver_1936.append(medal)	

	if medal[0] == 2014 and medal[3] == "Silver":
					silver_2014.append(medal)

print('austria won', len(silver_1928), 'silver medals in 1928')
print('austria won', len(silver_1936),  'silver medals in 1936')
print('austria won', len(silver_2014), 'silver medals in 2014')


print('processed', line_count, 'rows of data')

# filter 2010 based on years
#
# plot on a bar chart years =>
# how many medals for each year as  a percentage of the total
