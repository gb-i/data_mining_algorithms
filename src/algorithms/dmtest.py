# For random generation of numbers import randint
from random import randint, shuffle

# Simple generator for test plzs (40-40-20 biased), returns 1D array of plzs
def plzGen(entries):
	dataArray = []
	plz_lenght = 5
	for i in range(0, int(entries)):
		if i < round(entries * 0.4):
			plz = generateNumber(plz_lenght, 2)
		elif i >= round(entries * 0.4) and i < round(entries * 0.6):
			plz = generateNumber(plz_lenght, 9)
		elif i >= round(entries * 0.6) and i < round(entries * 0.9):
			plz = generateNumber(plz_lenght, 4)
		else:
			plz = generateNumber(plz_lenght, randint(0,9))
		dataArray.append(plz)
	shuffle(dataArray)
	return dataArray

# Function for generating the content of one single row randomly
def generateNumber(numberLenght, startingNumber):
	number = str(startingNumber)
	for length in range(0, numberLenght - 1):
		number = number + str(randint(0,9))
	return number

# Function for writing data into a file (content = string, nameChunkStart and namePartStart are for better naming)
# /testdata/ folder has to be created at this point
def writeFile(content, nameChunkStart, namePartStart):
	filenumber = int(nameChunkStart) + int(namePartStart)
	file = open("testdata/file" + str(filenumber) + ".txt", "w")
	for w in range(0, len(content)):
		file.write(content[w] + "\n")

# Function for generating 'entries'x int_lenght'-long numbers in 'clusters' clusters
def numGen(entries, cluster, int_lenght):
	dataArray = []
	clusterArray = []

	for cluster_num in range(0, cluster):
		clusterArray.append(randint(10,99))

	for item in range(0, entries):
		decider = randint(0, 2)
		if decider == 2:
			dataArray.append(generateNumber(int_lenght, randint(1,9)))
		else:
			cluster_decider = randint(0, cluster - 1)
			dataArray.append(generateNumber(int_lenght - 1, clusterArray[cluster_decider]))
	shuffle(dataArray)
	return dataArray
# Simple generator for test plzs (40-40-20 biased), returns 1D array of plzs
def plzGenNS(entries):
    dataArray = []
    plz_lenght = 5
    for i in range(0, int(entries)):
        if i < round(entries * 0.4):
            plz = generateNumber(plz_lenght, 2)
        elif i >= round(entries * 0.4) and i < round(entries * 0.8):
            plz = generateNumber(plz_lenght, 6)
        else:
            plz = generateNumber(plz_lenght, randint(0, 9))
        dataArray.append(plz)
    #i had to remove shuffle for the connectrion (age ==> plz) to work, else we would have 4 clusters
    # shuffle(dataArray)
    return dataArray  #


def ageGenNS(entries):
    dataArray = []
    age_lenght = 2
    for i in range(0, int(entries)):
        if i < round(entries * 0.4):
            age = generateNumber(age_lenght, 2)
        elif i >= round(entries * 0.4) and i < round(entries * 0.8):
            age = generateNumber(age_lenght, 5)
        else:
            age = generateNumber(age_lenght, randint(0, 9))
        dataArray.append(age)
    # shuffle(dataArray)
    return dataArray
