"""Phone number search example"""

import re

# TODO: Fix so that this only matches if it is not
# preceded or followed by additional digits
pat = r"(\d{3})-(\d{3})-(\d{4})"

s = "072-555-1591 is a fake phone number and my understanding is that the exchange 555 does not exist in any area code 123784917 7657657654 but 00000-000-0000000 here is another phone number 312-458-9999 and here is the end."

for m in re.finditer(pat,s):
    print("Found phone number between indices {} and {}:".format(
        m.start(),
        m.end()
    ))
    print("Area code: {}\nExchange: {}\nLine number: {}".format(
        m.group(1),
        m.group(2),
        m.group(3)
    ))
