"""
Author: David Flores Barbero
This script is with aim of make easier to create a csv
"""
import csv

print('Init of the script')

file = open("data.txt", "r")
text = file.read()
lines = text.split("\n")  # Leemos las lineas del fichero
fields = ["nombre", "email", "departamento", "telefono"]
personFields = []

sotanoArray = []
plantaBajaArray = []
primeraPlantaArray = []
segundaPlantaArray = []

for l in lines:  # Separate the lines in four arrays

    personFields = l.split(",")

    if len(personFields) == 5:

        if "P-3" in personFields[4]:
            sotanoArray.append(l)

        elif "PB" in personFields[4]:
            plantaBajaArray.append(l)

        elif "P1" in personFields[4]:
            primeraPlantaArray.append(l)

        elif "P2" in personFields[4]:
            segundaPlantaArray.append(l)


with open("sotano.csv", 'w') as myFile:
    wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
    wr.writerow(fields)  # write the first line of the CSV

    for s in sotanoArray:  # Loop the rest of lines and write in a CSV file
        personFields = s.split(",")
        personFields.pop()  # remove the last element of the array (the floor)
        wr.writerow(personFields)


with open("plantaBaja.csv", 'w') as myFile:
    wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
    wr.writerow(fields)  # write the first line of the CSV

    for pb in plantaBajaArray:  # Loop the rest of lines and write in a CSV file
        personFields = s.split(",")
        personFields.pop()  # remove the last element of the array (the floor)
        wr.writerow(personFields)

with open("primeraPlanta.csv", 'w') as myFile:
    wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
    wr.writerow(fields)  # write the first line of the CSV

    for p1 in primeraPlantaArray:  # Loop the rest of lines and write in a CSV file
        personFields = p1.split(",")
        personFields.pop()  # remove the last element of the array (the floor)
        wr.writerow(personFields)

with open("segundaPlanta.csv", 'w') as myFile:
    wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
    wr.writerow(fields)  # write the first line of the CSV

    for p2 in segundaPlantaArray:  # Loop the rest of lines and write in a CSV file
        personFields = p2.split(",")
        personFields.pop() # remove the last element of the array (the floor)
        wr.writerow(personFields)
