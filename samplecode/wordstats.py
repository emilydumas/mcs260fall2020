"""
Compute statistics on words in a given text
MCS 260 Fall 2020 Lecture 11 - Emily Dumas
"""

# We hard-code text because input() doesn't
# accept multiple lines.
# The following is from 7 CFR § 46.2(u)
text="""
Fresh fruits and fresh vegetables include all
produce in fresh form generally considered as
perishable fruits and vegetables, whether or 
not packed in ice or held in common or cold 
storage, but does not include those perishable 
fruits and vegetables which have been
manufactured into articles of food of a different
kind or character.
""".strip()

print("Reporting on the text:")
print(text+"\n")
print("Found:")
print(len(text.splitlines()),"lines")

# Note chain of str methods
words = text.replace(","," ").replace("."," ").split()
print(len(words),"words")

distinct_words = []
for w in words:
    w = w.lower()
    if w not in distinct_words:
        distinct_words.append(w)

print(len(distinct_words),"distinct words: ")

for w in distinct_words:
    print(w,end=" ")
print()