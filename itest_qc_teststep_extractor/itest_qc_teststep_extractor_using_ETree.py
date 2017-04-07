# procedure to read an iTest *.fftc test case and extract/display all the QualityCenter
# test step text.

__author__ = 'teggenbe'
from lxml import etree, objectify

parser = etree.XMLParser(remove_blank_text=True)
path = "C:\iTest_4.0\CND_TA5000_BBDLC_Ethernet\BBDLC Ethernet\Voice\Bulk_Call_(Parsed)_Sip_MGCP_GR303"
tree = etree.parse("n16s1-GR303-A2Combo-BulkCall-via-SM025Gx.fftc")
catalogue = tree.getroot()

for qualityCenterStepInfo in catalogue.iter("qualityCenterStepInfo"):
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





