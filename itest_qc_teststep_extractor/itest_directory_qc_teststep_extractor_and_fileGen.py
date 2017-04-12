# procedure to read an iTest *.fftc test case and extract/display all the QualityCenter
# test step text.
import os
__author__ = 'teggenbe'
from lxml import etree, objectify

#Change the 'path' to where the *.fftc test-cases are you want to parse
path = "C:/iTest_4.0/CND_TA5000_BBDLC_Ethernet/BBDLC Ethernet/Voice/Bulk_Call_(Parsed)_Sip_MGCP_GR303/"
#get a list of all the files in that directory (assumes they will be *.fftc files only)
file_listing = os.listdir(path)

for each_file in file_listing:
    file_to_parse = path + each_file
    tree = etree.parse(file_to_parse)
    itest_test_case = tree.getroot()
    #create a new *.txt file using the same name from the *.fftc filename
    filename = ('C:/temp/%s.txt' % each_file)
    f = open(filename, 'a')
    f.truncate()    #  if re-running, delete everything in the old file.
    #Parse each 'quality center' step and get the relevant 'step' information
    for qualityCenterStepInfo in itest_test_case.iter("qualityCenterStepInfo"):
        try:
            stepname = qualityCenterStepInfo.get('stepName')
        except AttributeError:
            stepname = "BLANK"
        try:
            description = qualityCenterStepInfo.find("description").text
        except AttributeError:
            description = "BLANK"
        try:
            expectedResult = qualityCenterStepInfo.find("expected_result").text
        except AttributeError:
            expectedResult = "BLANK"

        #optionally, print step info to python console
        print "Step Name:\n %s" % stepname
        print "Description:\n %s" % description
        print "Expected Result:\n %s \n" % expectedResult
        #write step info. to new file
        f.write("\n")
        f.write ("Step Name: \n" +  stepname + "\n")
        f.write ("Description: \n" + description + "\n")
        f.write ("Expected: \n" + expectedResult + "\n")

f.close()




