## Script converts yearly listings to individual files for localities

dept_data = {}

for year in range(1984, 2013):
	curr_file = open(str(year)+".csv", 'r')
	for line in curr_file:
		line_arr = line.split(",")
		dept = line_arr[0]
		line_arr[0] = str(year)

		if dept not in dept_data:
			dept_data[dept] = []

		dept_data[dept].append(str(line_arr)[1:-1])


for key in dept_data:
	curr_output = open("output/" + key.replace(' ', '_') +".csv", 'w')
	curr_output.write("Year,State,Months,Population,Violent crime total,Murder and nonnegligent Manslaughter,Forcible rape,Robbery,Aggravated assault,Property crime total,Burglary,Larceny-theft,Motor vehicle theft,Violent Crime rate,Murder and nonnegligent manslaughter rate,Forcible rape rate,Robbery rate,Aggravated assault rate,Property crime rate,Burglary rate,Larceny-theft rate,Motor vehicle theft rate,\n")

	for line in dept_data[key]:
		curr_output.write(line[:-3].replace("'", '').replace('\n','') + '\n')

	curr_output.close()

