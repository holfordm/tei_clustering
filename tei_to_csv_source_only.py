# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import glob
import csv






#opens csv file for output
csvfile = open('output.csv', 'w', newline='', encoding="utf8")
csvwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow(
    ["filename", "source"])

corpus = glob.glob('../medieval-mss/collections/*/*.xml')

#loop through xml files
for file in corpus:
    
    with open(file, 'r', encoding="utf8") as xml:
        
        soup=bs(xml, 'lxml', from_encoding = 'utf-8')
        #soup = bs(soup.decode('utf-8', 'ignore'))
        #print(soup)
        print (file)

        filename=file.rpartition("/")[-1]

        
        source=""
        try:
            source=soup.find("source")
        except:
            source = ""
        print (source)

        
        csvwriter.writerow(
            [filename, source])

csvfile.close()

