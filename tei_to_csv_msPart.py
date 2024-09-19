# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import glob
import csv






#opens csv file for output
csvfile = open('output.csv', 'w', newline='', encoding="utf8")
csvwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow(
    ["filename", "leaf-dim-unit", "leaf-height", "leaf-width", "writtenHeight", "writtenWidth", "LeafDivWritten"])

corpus = glob.glob('../medieval-mss/collections/*/*.xml')

# verbose but works
def getDimension(dimension):
    try:
        maxVal = dimension['max']
    except:
        maxVal = "0"

    try:
        minVal = dimension['min']
    except:
        minVal = "0"

    try:
        quantity = dimension['quantity']
    except:
        quantity = "0"

    
    if int(maxVal) > 0:            
        value = (float(dimension['max']) + float(dimension['min'])) / 2
    elif int(quantity) > 0:
        value = dimension['quantity']
    else:
        value = dimension.get_text()

    return value


#loop through xml files
for file in corpus:
    
    with open(file, 'r', encoding="utf8") as xml:

        #changed from lxml to xml. maybe i don't have lxml installed? 
        soup=bs(xml, 'xml')
       
        #print(soup)
        print (file)

        filename=file.rpartition("/")[-1]

## need to escape commas etc.
##        content = ""
##        try:
##            content = soup.find("msContents").get_text()
##        except:
##            content = ""

        #dimensions for the ms as a whole if given


        #leaf dimensios
        #1 unit
        dimension_unit=""
        try:
            dimension_unit = soup.find("dimensions", {"type": "leaf"})["unit"]
        except:
            dimension_unit = ""
        print(dimension_unit)

        #leaf dimensios

        # note that this and the following need to have type[binding] added at some point
        
        #2 height
        height = ""
        try:
            height = soup.find("dimensions", {"type": "leaf"}).find("height")
            print(height)

            
            height = getDimension(height)
            print(height)

            #height=height.get_text()
            #if "-" in height:
            #    height = height.rpartition("-")[0]
            
        except:
            height = ""
        print(height)

        #leaf dimensios
        #3 width

        width = ""

        
        try:
            width = soup.find("dimensions", {"type": "leaf"}).find("width")
            print(width)
            width =  getDimension(width)
            print(width)  
        except:
            width = ""


        #need to allow for column space

        writtenHeight = ""
        try:
            writtenHeight = soup.find("dimensions", {"type": ("ruled", "written", "column")}).find("height")
                 
            writtenHeight = getDimension(writtenHeight)
            
            print(writtenHeight)
        except:
            writtenHeight = ""

        writtenWidth = ""
        try:
            writtenWidth = soup.find("dimensions", {"type": ("ruled", "written")}).find("width")
            writtenWidth = getDimension(writtenWidth)
        except:
            writtenWidth = ""

        #todo: columns and lines


        leafDivWritten = ""
        try:
            leafDivWritten = float(height) / float(writtenHeight)
        except:
            leafDivWritten = ""
        
        csvwriter.writerow(
            [filename, dimension_unit, height, width, writtenHeight, writtenWidth, leafDivWritten])


        #cycle through msParts

        
        
##        msParts = soup.find_all("msPart")
##
##        
##
##        for msPart in msParts:
##            idno = msPart.find("idno")
##            idno = idno.get_text()
##            print(idno)
##
##            writtenHeight = ""
##
##
##            try:
##                writtenHeight = msPart.find("dimensions", {"type": ("ruled", "written")}).find("height")
##                 
##                writtenHeight = getDimension(writtenHeight)
##                
##                print(writtenHeight)
##            except:
##                writtenHeight = ""
##
##            writtenWidth = ""
##
##            try:
##                writtenWidth = msPart.find("dimensions", {"type": ("ruled", "written")}).find("width")
##                writtenWidth = getDimension(writtenWidth)
##            except:
##                writtenWidth = ""
##
##        
##            csvwriter.writerow(
##                [idno, "", height, width, writtenHeight, writtenWidth])

csvfile.close()

