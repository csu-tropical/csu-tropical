import sys

id = str(input('Input paper ID: '))
year = str(input('Enter submission year: ')) 
title = str(input('Enter paper title: '))
author1 = str(input('Enter 1st author: '))
author2 = str(input('Enter 2nd author: '))
author3 = str(input('Enter 3rd author: '))
authors = str(input('Enter all authorsi: '))
journal = str(input('Enter journal name: '))
others = str(input('Enter paper status (i.e. sumbitted, in-press, published: '))
doi = 'false'
keypoint1 = 'false'
keypoint2 = 'false'
keypoint3 = 'false'
abstract = 'false'
summary = 'false'
image = 'false'
caption = 'false'
acknowledgement = 'false'
bibtex = 'false'
pdf = 'false'
keyword1 = 'false'
keyword2 = 'false'
keyword3 = 'false'

orig_stdout = sys.stdout

filename = id + '.yml'
f = open(filename, 'w')
sys.stdout = f
f.write("- id: " + id + "\n")
f.write("  year: " + year + "\n")
f.write("  title: " + title + "\n")
f.write("  author1: " + author1 + "\n")
f.write("  author2: " + author2 + "\n")
f.write("  author3: " + author3 + "\n")
f.write("  authors: " + authors + "\n")
f.write("  journal: " + journal + "\n")
f.write("  others:  " + others + "\n")
f.write("  doi: " + doi + "\n")
f.write("  keypoint1: " + keypoint1 + "\n")
f.write("  keypoint2: " + keypoint2 + "\n")
f.write("  keypoint3: " + keypoint3 + "\n")
f.write("  abstract: " + abstract + "\n")
f.write("  summary: " + summary + "\n")
f.write("  image: " + image + "\n")
f.write("  acknowledgement: " + acknowledgement + "\n")
f.write("  bibtex: " + bibtex + "\n")
f.write("  pdf: " + pdf + "\n")
f.write("  keyword1: " + keyword1 + "\n")
f.write("  keyword2: " + keyword2 + "\n")
f.write("  keyword3: " + keyword3 + "\n")

sys.stdout = orig_stdout
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())
print(filename)
