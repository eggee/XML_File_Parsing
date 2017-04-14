#modified into modules to
# 1) get the 'test_run_info.'
#Use these command line parameters in the initial test call
#C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml N26S3-48p

import xml.etree.ElementTree as ET
import sys

def get_test_run_info(Result_XML):
    tree = ET.parse(Result_XML)
    root = tree.getroot()
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


start_time, stop_time, run_time = get_test_run_info(Result_XML)

print start_time
print stop_time
print run_time

