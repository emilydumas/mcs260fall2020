"""
Fetch a URL, decode as text, and print to the terminal
"""

import urllib.request
import sys

# First command line argument is the url
url = sys.argv[1]

# Make the HTTP GET request
res = urllib.request.urlopen(url)

# Read the encoding from the headers
enc = res.headers.get_content_charset()

# Decode and print
print(res.read().decode(encoding=enc))
