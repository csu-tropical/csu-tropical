import sys

id = str(input('Input paper ID: '))
year = str(input('Enter submission year: ')) 
title = str(input('Enter paper title: '))
author1 = str(input('Enter 1st author: '))
author2 = str(input('Enter 2nd author: '))
author3 = str(input('Enter 3rd author: '))
authors = str(input('Enter all authors: '))
journal = str(input('Enter journal name: '))
others = str(input('Enter paper status (submitted, published): '))
doi = str(input('DOI: '))
keypoint1 = str(input('keypoint1 : '))
keypoint2 = str(input('keypoint2 : '))
keypoint3 = str(input('keypoint3 : '))
abstract = str(input('Abstract : '))
summary = str(input('Summary : ')) 
image = str(input('image : ../Publications/figures/'))
caption = str(input('caption :'))
acknowledgement = str(input('aknowledgement :'))
bibtex = str(input('bibtex : ../Publications/bibtex/'))
pdf = str(input('pdf file ../Publications/papers/'))
keyword1 = str(input('keyword1 : '))
keyword2 = str(input('keyword2 :'))
keyword3 = str(input('keyword3 :'))

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
f.write("  image: ../Publications/figures/" + image + "\n")
f.write("  caption: " + caption + "\n")
f.write("  acknowledgement: " + acknowledgement + "\n")
f.write("  bibtex: ../Publications/bibtex/" + bibtex + "\n")
f.write("  pdf: ../Publications/papers/" + pdf + "\n")
f.write("  keyword1: " + keyword1 + "\n")
f.write("  keyword2: " + keyword2 + "\n")
f.write("  keyword3: " + keyword3 + "\n")

sys.stdout = orig_stdout
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())
print(filename)

