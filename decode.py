print("Starting!")

# create temp.txt if not exist with write mode
testFile = open("temp.txt", "w+")

# Reading log file
with open("logfile.log", 'r') as logData:

	for logLine in logData:
		# Write data in temp.txt file
		testFile.write(logLine.replace('\n',''))

# Open temp.txt file in read mode
newTestFile = open("temp.txt", "r+")	

for newLine in newTestFile:
	# Take a all data of temp.txt file into fwrite variable
	fwrite = newLine.replace('01 03', '\n01 03')

# Open temp.txt file with truncate all data
file = open("temp.txt", "w+")

# Write data into temp.txt file
file.write(fwrite)

print("It works!")
