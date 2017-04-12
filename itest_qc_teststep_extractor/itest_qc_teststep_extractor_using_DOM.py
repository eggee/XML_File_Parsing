# procedure to read an iTest *.fftc test case and extract all the QualityCenter
# test step text.

__author__ = 'teggenbe'
from xml.dom import minidom

itest_case = minidom.parse("025G1_Cross-Slot_LAG_2x10Gig_to_Cisco.fftc")
# Get all QualityCenterStepInfo Tags, is written to a 'list'
qcstepinfo = itest_case.getElementsByTagName("qualityCenterStepInfo")

for qualityCenterStepInfo in qcstepinfo:
    # stepname = qualityCenterStepInfo.getElementsByTagName("stepName")[0].firstChild.data
    stepname = qualityCenterStepInfo._attrs[u'stepName'].nodeValue
    description = qualityCenterStepInfo.getElementsByTagName("description")[0].firstChild.data
    expectedResult = qualityCenterStepInfo.getElementsByTagName("expected_result")[0].firstChild.data

    print "Step Name:\n %s" % stepname
    print "Description:\n %s" % description
    print "Expected Result:\n %s \n" % expectedResult



