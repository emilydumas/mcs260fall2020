"""
Roll dice using API at roll.diceapi.com
"""

import urllib.request
import sys
import json

# First command line argument is the dice specification
dice_spec = sys.argv[1]

# Make the HTTP GET request
res = urllib.request.urlopen("http://roll.diceapi.com/json/"+dice_spec)
rolldata = json.loads(res.read())
res.close()

# Now the dice roll data is in the dictionary rolldata

# Print the rolls
print("The following numbers were rolled:")
for x in rolldata["dice"]:
    print(x["value"])