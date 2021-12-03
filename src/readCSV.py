from imports import *

def read():
    file = open("../july_stats.csv")
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    deaths = []
    for row in rows:
        deaths.append((float) (row[8]))

    return deaths
