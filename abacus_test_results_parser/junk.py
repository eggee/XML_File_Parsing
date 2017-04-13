import xml.etree.ElementTree as ET
import sys

def get_test_run_info(Result_XML):
    # neighbor.attrib.values()[1] = 0
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



Result_XML = "C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml"
script = "N26S3-48p"
x = get_test_run_info(Result_XML)

print x