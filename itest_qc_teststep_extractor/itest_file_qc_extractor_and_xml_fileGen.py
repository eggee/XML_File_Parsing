# procedure to read an iTest *.fftc test case and extract/display all the QualityCenter
# test step information and write it to an *.xml file.
import os
__author__ = 'teggenbe'
from lxml import etree, objectify

itest_file = "025G1_Cross-Slot_LAG_2x10Gig_to_Cisco.fftc"
#create a new *.xml file using the same name from the *.fftc new_file
file_name = itest_file.split('.')
file_name = file_name[0]
new_file = ('%s.xml' % file_name)
f = open(new_file, 'a')
f.truncate()    #  if re-running, delete everything in the old file.
#Parse each 'quality center' step and get the relevant 'step' information
# write the opening xml tag for 'qc_steps'
f.write("<qc_steps >\n")

tree = etree.parse(itest_file)
itest_test_case = tree.getroot()

step_num = 1
#TODO: check to see if attribute is 'true', otherwise, skip getting the qc info for that iteration
for qualityCenterStepInfo in itest_test_case.iter("qualityCenterStepInfo"):
    is_step_enabled = qualityCenterStepInfo.get('associateWithDesignStep')
    #is_step_enabled = 'true'
    if is_step_enabled:
        try:
            stepname = qualityCenterStepInfo.get('stepName')
        except AttributeError:
            stepname = "BLANK"
        try:
            description = qualityCenterStepInfo.find("description").text
        except AttributeError:
            description = "BLANK"
        try:
            expected_result = qualityCenterStepInfo.find("expected_result").text
        except AttributeError:
            expected_result = "BLANK"

        #write the step information in an XML format
        stepname = "  <step name =\"Name\">%s\"</step>" % stepname
        description = "  <step name =\"Description\">%s</step>" % description
        expected = "  <step name =\"Expected\">%s</step>" % expected_result
        #write to file
        f.write("\t<Step>\n")
        f.write("\t  <step name =\"number\">" + str(step_num) + "</step>\n")
        f.write("\t" + stepname + "\n")
        f.write("\t" + description + "\n")
        f.write("\t" + expected + "\n")
        f.write("\t</Step>\n")
        step_num += 1
#close the xml section for 'qc_steps'
f.write("</qc_steps >")
f.close()




