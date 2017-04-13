#modified into modules to
# 1) get the 'script-comment' results
# 2) get the 'test_run_info.'
#Use these command line parameters in the initial test call
#C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml N26S3-48p

import xml.etree.ElementTree as ET
import sys

# def open_the_xml_report(Result_XML):
#     try:
#         XML = open(Result_XML)
#     except IOError:
#         sys.exit("The file does not exist, exiting gracefully")
#
#     set_num = 0
#     tree = ET.parse(Result_XML)
#     root = tree.getroot()

def get_test_run_info(Result_XML):
    # neighbor.attrib.values()[1] = 0
    # tree = ET.parse(Result_XML)
    # root = tree.getroot()
    #Search the 'root' for a tag called 'test-status'
    for neighbor in root.iter('test-status'):
        test_status = neighbor.attrib
        start_time_with_space = test_status.get('start')
        start_time = start_time_with_space.replace(" ", "_")
        stop_time_with_space = test_status.get('end')
        stop_time = stop_time_with_space.replace(" ", "_")
        run_time = test_status.get ('elapsed')

# def get_script_results_info(script):
#     # GETS THE 'set #' FOR THE GIVEN Script-Name
#     for neighbor in root.iter('set'):
#         if neighbor[3][2].text == script:
#             set_num = neighbor.attrib.values()[0]
#
#     # CHECK IF 'set num' WAS UPDATED OR NOT
#     if set_num == 0:
#         sys.exit("Given Script is not found in XML file, Hence exiting gracefully")
#
#     if set_num == '':
#         sys.exit("Set Number is not defined in given Script,Hence Exiting gracefully")
#
#     for neighbor in root.iter('stat-channels'):
#         if neighbor.attrib.values()[1] == set_num:
#             total_channel_stats = neighbor[0][0].attrib
#             single_channel_stats = neighbor[1].attrib
#             CC = total_channel_stats.get('percent-call-completions')
#             SC = total_channel_stats.get("percent-script-completions")
#             call_attemps_per_sec = total_channel_stats.get ('call-attempts-per-sec')
#             Total_call_attempts = total_channel_stats.get('call-attempts')
#             Total_Script_attempts = total_channel_stats.get ('script-attempts')
#             call_cycles = single_channel_stats.get ('call-attempts')
#
#         if neighbor.attrib.values()[1] == 0:
#             sys.exit("Set Number is not there in Result XMl File")


Result_XML = "C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml"
script = "N26S3-48p"
x = get_test_run_info(Result_XML)

print x
#
# print '<?xml version="1.0" encoding="ISO-8859-1"?>'
# print "<ParsingResults>"
# print ' ' "<Test_Information>"
# print '     ' '<' + "Test_start_time" + '>' + start_time + '</' + "Test_start_time" + '>'
# print '     ' '<' + "Test_stop_time" + '>' + stop_time + '</' + "Test_stop_time" + '>'
# print '     ' '<' + "Test_run_time" + '>' + run_time + '</' + "Test_run_time" + '>'
# print ' ' "</Test_Information>"
# print ' ' "<Abacus_Data>"
# print '     ' '<' + "call_cycles" + '>' + call_cycles + '</' + "call_cycles" + '>'
# print '     ' '<' + "set_num" + '>' + set_num + '</' + "set_num" + '>'
# print ' ' "</Abacus_Data>"
# print ' ' "<" + script + "_Results>"
# print '     ' '<' + "Script_Completion_Percentage" + '>' + SC + '</' + "Script_Completion_Percentage" + '>'
# print '     ' '<' + "Call_Completion_Percentage" + '>' + CC + '</' + "Call_Completion_Percentage" + '>'
# print '     ' '<' + "call_attemps_per_sec" + '>' + call_attemps_per_sec + '</' + "call_attemps_per_sec" + '>'
# print '     ' '<' + "Total_call_attempts" + '>' + Total_call_attempts + '</' + "Total_call_attempts" + '>'
# print '     ' '<' + "Total_Script_attempts" + '>' + Total_Script_attempts + '</' + "Total_Script_attempts" + '>'
# print ' ' "</" +script + "_Results>"
# print "</ParsingResults>"