# procedure to read a directory in iTest (*.fftc test cases) and extract/display all the QualityCenter
# test step information and write each to it's own *.xml file.
import os
__author__ = 'teggenbe'
from lxml import etree, objectify

#Change the 'path' to where the *.fftc test-cases are you want to parse
path = "C:/iTest_4.0/CND_TA5000_BBDLC_Ethernet/BBDLC Ethernet/Voice/Bulk_Call_(Parsed)_Sip_MGCP_GR303/"
#get a list of all the files in that directory (assumes they will be *.fftc files only)
file_listing = os.listdir(path)

#for each file in the given directory, parse it to search for 'qualitycenter' step information
for each_file in file_listing:
    file_to_parse = path + each_file
    tree = etree.parse(file_to_parse)
    itest_test_case = tree.getroot()
    #create a new *.xml file using the same name from the *.fftc new_file
    file_name = each_file.split('.')
    file_name = file_name[0]
    new_file = ('C:/temp/%s.xml' % file_name)
    f = open(new_file, 'a')
    f.truncate()    #  if re-running, delete everything in the old file.
    #Parse each 'quality center' step and get the relevant 'step' information
    # write the opening xml tag for 'qc_steps'
    f.write("<qc_steps >\n")
    #start a counter to invrement the 'step number' tag
    step_num = 1
    #TODO: check to see if attribute is 'true', otherwise, skip getting the qc info for that iteration
    for qualityCenterStepInfo in itest_test_case.iter("qualityCenterStepInfo"):
        is_step_enabled = qualityCenterStepInfo.get('associateWithDesignStep')
        # is_step_enabled = 'true'
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
            #increment the 'step number' tag value by 1
            step_num += 1
    #close the xml section for 'qc_steps'
    f.write("</qc_steps >")
    f.close()




