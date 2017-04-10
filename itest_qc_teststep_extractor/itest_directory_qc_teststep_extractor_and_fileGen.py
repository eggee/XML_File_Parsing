# procedure to read an iTest *.fftc test case and extract/display all the QualityCenter
# test step text.
import os
__author__ = 'teggenbe'
from lxml import etree, objectify

#parser = etree.XMLParser(remove_blank_text=True)
path = "C:/iTest_4.0/CND_TA5000_BBDLC_Ethernet/BBDLC Ethernet/Voice/Bulk_Call_(Parsed)_Sip_MGCP_GR303/"
# test_case = "n16s2-GR303-V2Combo-BulkCall-via-SM025Gx.fftc"
file_listing = os.listdir(path)

for each_file in file_listing:
    file_to_parse = path + each_file
    tree = etree.parse(file_to_parse)
    itest_test_case = tree.getroot()

    filename = ('C:/temp/%s.txt' % each_file)
    f = open(filename, 'a')
    f.truncate()
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
            expectedResult = qualityCenterStepInfo.find("expectedResult").text
        except AttributeError:
            expectedResult = "BLANK"

        print "Step Name:\n %s" % stepname
        print "Description:\n %s" % description
        print "Expected Result:\n %s \n" % expectedResult

        f.write("\n")
        f.write ("Step Name: \n" +  stepname + "\n")
        f.write ("Description: \n" + description + "\n")
        f.write ("Expected: \n" + expectedResult + "\n")

f.close()




