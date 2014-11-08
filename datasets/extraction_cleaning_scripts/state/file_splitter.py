import re

file_in = open("../CrimeStatebyState.csv", 'r')
file_out = 0
state = ""

for line in file_in:
	match = re.search(r'^Estimated crime in [A-Z][a-z]*', line)
	if(match):
		try:
			file_out.close()
		except:
			print "yo"

		state = line[19:-1]
		file_out = open(state+".csv", 'w')
		file_out.write("Year,Population,Violent crime total,Murder and nonnegligent Manslaughter,Forcible rape,Robbery,Aggravated assault,Property crime total,Burglary,Larceny-theft,Motor vehicle theft,Violent Crime rate,Murder and nonnegligent manslaughter rate,Forcible rape rate,Robbery rate,Aggravated assault rate,Property crime rate,Burglary rate,Larceny-theft rate,Motor vehicle theft rate,")
	elif(len(line.split(",")) >= 3):
		file_out.write(line)