"""
Author: David Flores Barbero
This script is with aim of make easier to create a csv
"""
import csv

print('Init of the script')

file = open("data.txt", "r")
text = file.read()
lines = text.split("\n")  # Leemos las lineas del fichero
fields = ["nombre", "email", "departamento", "telefono", "planta"]

with open("result.csv", 'w') as myFile:

    wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
    wr.writerow(fields) # write the first line of the CSV

    for l in lines: # Loop the rest of lines and write in a CSV file
        fields = l.split(",")
        wr.writerow(fields)

