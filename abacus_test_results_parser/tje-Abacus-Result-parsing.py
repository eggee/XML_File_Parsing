#modified into modules to
# 1) get the 'script-comment' results
# 2) get the 'test_run_info.'
#Use these command line parameters in the initial test call
#C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml N26S3-48p

import xml.etree.ElementTree as ET
import sys

def open_the_xml_report(Result_XML):
    tree = ET.parse(Result_XML)
    root = tree.getroot()

    return root

def get_the_setnum(root, script):
    # GETS THE 'set #' FOR THE GIVEN Script-Name
    for neighbor in root.iter('set'):
        if neighbor[3][2].text == script:
            set_num = neighbor.attrib.values()[0]

    #CHECK IF 'set num' WAS UPDATED OR NOT
    if set_num == 0 :
        sys.exit("Given Script is not found in XML file, Hence exiting gracefully")

    if set_num == '':
        sys.exit("Set Number is not defined in given Script,Hence Exiting gracefully")

    return set_num

def get_test_run_info(root):
    #Search the 'root' for a tag called 'test-status'
    for neighbor in root.iter('test-status'):
        test_status = neighbor.attrib
        start_time_with_space = test_status.get('start')
        start_time = start_time_with_space.replace(" ", "_")
        stop_time_with_space = test_status.get('end')
        stop_time = stop_time_with_space.replace(" ", "_")
        run_time = test_status.get ('elapsed')

    return start_time, stop_time, run_time

def get_script_results_info(set_num, root):
    # for the given 'set_num" - get the results
    #Search for 'stat-channels', then compare it's 'set_num'
    for neighbor in root.iter('stat-channels'):
        if neighbor.attrib.values()[1] == set_num:
            total_channel_stats = neighbor[0][0].attrib
            single_channel_stats = neighbor[1].attrib
            percent_callcompletions = total_channel_stats.get('percent-call-completions')
            percent_scriptcompletions = total_channel_stats.get("percent-script-completions")
            call_attemps_per_sec = total_channel_stats.get ('call-attempts-per-sec')
            Total_call_attempts = total_channel_stats.get('call-attempts')
            Total_Script_attempts = total_channel_stats.get ('script-attempts')
            call_cycles = single_channel_stats.get ('call-attempts')

        if neighbor.attrib.values()[1] == 0:
            sys.exit("Set Number is not there in Result XMl File")

    return percent_callcompletions,percent_scriptcompletions,call_attemps_per_sec,Total_call_attempts,Total_Script_attempts,call_cycles

#MAIN
def main():
    Result_XML = "C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml"
    script = "N26S3-48p"
    CC = float
    root = open_the_xml_report(Result_XML)
    set_num = get_the_setnum(root, script)

    start_time, stop_time, run_time = get_test_run_info(root)
    print "\n *** Abacus Results for %s ***\n" % script
    print "Start Time:\t %s" % start_time
    print "Stop Time:\t %s" % stop_time
    print "Run  Time:\t %s \n" % run_time

    CC, SC, call_attemps_per_sec, total_call_attempts, total_script_attempts, call_cycles = get_script_results_info(set_num, root)
    print "Percent Call Completions:\t %s" % CC
    print "Percent Script Completions:\t %s" % SC
    print "Call Attempts per Second:\t %s" % call_attemps_per_sec
    print "Total Call Attempts:\t\t %s" % total_call_attempts
    print "Total Script Attempts:\t\t %s" % total_script_attempts
    print "Total Call Attempts:\t\t %s" % call_cycles

#Run Main
main()
