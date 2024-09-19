# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import glob
import csv



#test version for Douce manuscripts.


#opens csv file for output
csvfile = open('tei-msItem-count.csv', 'w', newline='', encoding="utf8")
csvwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow(
    ["filename", "SCN", "items"])

corpus = glob.glob('../medieval-mss/collections/Douce/*.xml')

#loop through xml files
for file in corpus:
    
    with open(file, 'r', encoding="utf8") as xml:
        
        soup=bs(xml, 'xml', from_encoding = 'utf-8')
        #soup = bs(soup.decode('utf-8', 'ignore'))
        #print(soup)


        
        shelfmark = ""
        try:
            shelfmark = soup.find('title').get_text()
        except:
            shelfmark = ""

        print(shelfmark)    

        SCN = ""
        try:
            SCN = soup.find('idno', {'type':'SCN'}).get_text()
        except:
            SCN = ""

        contents = ""
        try:
            msContents = soup.find_all('msContents')
        except:
            msContents = ""

        
        totalItems = 0

        for ms in msContents:
            msItems = ms.find_all('msItem')
            #print(msItems)
            total = len(msItems)
            totalItems = totalItems + total
            #print(totalItems)
            
        #totalItems = len(contents)                      
                              


        
        csvwriter.writerow([shelfmark, SCN, totalItems])

csvfile.close()

