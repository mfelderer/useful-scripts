# pip install bibtexparser
import bibtexparser

# insert a concrete bib file here to load it as dictionary
with open('XYZ.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# extract titles of concrete entries but not proceedings titles and clean the titles
for entry in bib_database.entries:
    if not (entry['ENTRYTYPE'] == 'proceedings'): 
        print(entry['title'].replace("{"," ").replace("}"," ").replace("\n"," "))
