#modified into modules to
# 1) get the 'test_run_info.'
#Use these command line parameters in the initial test call
#C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml N26S3-48p


import xml.etree.ElementTree as ET
import sys

def open_the_xml_report(Result_XML):
    set_num = 0
    tree = ET.parse(Result_XML)
    root = tree.getroot()

    # GETS THE 'set #' FOR THE GIVEN Script-Name
    for neighbor in root.iter('set'):
        if neighbor[3][2].text == script:
            set_num = neighbor.attrib.values()[0]

    #CHECK IF 'set num' WAS UPDATED OR NOT
    if set_num == 0 :
        sys.exit("Given Script is not found in XML file, Hence exiting gracefully")

    if set_num == '':
        sys.exit("Set Number is not defined in given Script,Hence Exiting gracefully")

    return root

def get_test_run_info(Result_XML):
    #Search the 'root' for a tag called 'test-status'
    for neighbor in root.iter('test-status'):
        test_status = neighbor.attrib
        start_time_with_space = test_status.get('start')
        start_time = start_time_with_space.replace(" ", "_")
        stop_time_with_space = test_status.get('end')
        stop_time = stop_time_with_space.replace(" ", "_")
        run_time = test_status.get ('elapsed')

    return start_time, stop_time, run_time

#MAIN
Result_XML = "C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml"
script = "N26S3-48p"

root = open_the_xml_report(Result_XML)

start_time, stop_time, run_time = get_test_run_info(root)

print start_time
print stop_time
print run_time

