"""Analyze building violation data from Chicago
city data portal.
MCS 260 Fall 2020 Lecture 30 example
"""

import csv
import os
import sys

# The next line needs to be set to the path and
# filename of the data file from 
# https://data.cityofchicago.org/Buildings/Building-Violations/22u3-xenr
datafn = r"Building_Violations.csv"

# Added after lecture: Warn the user if the file doesn't
# exist.
if not os.path.exists(datafn):
    print("ERROR: The file '{}' does not exist.")
    print("If the building violations CSV file is located")
    print("elsewhere, edit the source file to specify the")
    print("location in the variable `datafn`.  The CSV")
    print("file can be downloaded from:")
    print("  https://data.cityofchicago.org/Buildings/Building-Violations/22u3-xenr")
    sys.exit()

f = open(datafn,"r",encoding="UTF-8",newline="")
csvdata = csv.DictReader(f)

# Checked google maps for the lat,long of the
# corners of campus (approximated as a rectangle)
# NE_corner 41.875530,-87.645578
# SW_corner 41.867077,-87.651010

for row in csvdata:
    try:
        latitude = float(row["LATITUDE"])
        longitude = float(row["LONGITUDE"])
    except Exception:
        continue

    # Abort this iteration if the location is
    # outside the rectangle that approximates
    # the UIC campus
    if latitude > 41.875530:
        continue
    if latitude < 41.867077:
        continue
    if longitude > -87.645578:
        continue
    if longitude < -87.651010:
        continue

    # Abort this iteration if the report is not a complaint
    if row["INSPECTION CATEGORY"] != "COMPLAINT":
        continue
    
    # Abort this iteration if the report is about signage
    if "SIGN" in row["VIOLATION DESCRIPTION"]:
        continue

    # IF we make it here, then the report is for a 
    # location that is on the UIC east campus
    # for a violation based on a complaint
    # that is not about signs.  Print the full
    # violation record for review.
    print(row)

