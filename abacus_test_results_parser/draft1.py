#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      teggenbe
#
# Created:     06/06/2016
# Copyright:   (c) teggenbe 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os
from xml.etree import ElementTree

#specify the XML file into a variable
file_name = 'BBDLC_System_InterMix_MGCP_SIP_GR303.xml'
#specify the 'path' to said file.
full_file = os.path.abspath(os.path.join('c:\data', file_name))
#display the full path an visually verify
print(full_file)

#load the XML into 'dom' from the ElementTree class
#dom = ElementTree.parse(full_file)

#execute 'queries' on the 'dom'
#courses = dom.findall('course/title')

#for c in courses:
#    print(c)
