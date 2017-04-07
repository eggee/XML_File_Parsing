
import xml.etree.ElementTree as ET
import sys

#Use these command line parameters in the initial test call
#C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml N26S3-48p

argCount = len(sys.argv)
if argCount == 3:
    Result_XML = sys.argv[1]
    script = sys.argv[2]
else:
    sys.exit("Insufficient number of arguments, abort execution")
try:
    XML = open(Result_XML)
except IOError:
    sys.exit("The file does not exist, exiting gracefully")
##f = open(Result_XML,'r')
##x = f.readlines()
##y = x[:x.index('\t</partition-and-timing-settings>\n')+1]
##f2 = open(Result_XML, 'w')
##for z in y:
##    f2.write(str(z))
##f2.write("</report>")
##f2.close()

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

neighbor.attrib.values()[1] = 0
for neighbor in root.iter('test-status'):
    test_status = neighbor.attrib
    start_time_with_space = test_status.get('start')
    start_time = start_time_with_space.replace(" ", "_")
    stop_time_with_space = test_status.get('end')
    stop_time = stop_time_with_space.replace(" ", "_")
    run_time = test_status.get ('elapsed')


for neighbor in root.iter('stat-channels'):
    if neighbor.attrib.values()[1] == set_num:
        total_channel_stats = neighbor[0][0].attrib
        single_channel_stats = neighbor[1].attrib
        CC = total_channel_stats.get('percent-call-completions')
        SC = total_channel_stats.get("percent-script-completions")
        call_attemps_per_sec = total_channel_stats.get ('call-attempts-per-sec')
        Total_call_attempts = total_channel_stats.get('call-attempts')
        Total_Script_attempts = total_channel_stats.get ('script-attempts')
        call_cycles = single_channel_stats.get ('call-attempts')


if neighbor.attrib.values()[1] == 0:
    sys.exit("Set Number is not there in Result XMl File")

print '<?xml version="1.0" encoding="ISO-8859-1"?>'
print "<ParsingResults>"
print ' ' "<Test_Information>"
print '     ' '<' + "Test_start_time" + '>' + start_time + '</' + "Test_start_time" + '>'
print '     ' '<' + "Test_stop_time" + '>' + stop_time + '</' + "Test_stop_time" + '>'
print '     ' '<' + "Test_run_time" + '>' + run_time + '</' + "Test_run_time" + '>'
print ' ' "</Test_Information>"
print ' ' "<Abacus_Data>"
print '     ' '<' + "call_cycles" + '>' + call_cycles + '</' + "call_cycles" + '>'
print '     ' '<' + "set_num" + '>' + set_num + '</' + "set_num" + '>'
print ' ' "</Abacus_Data>"
print ' ' "<" + script + "_Results>"
print '     ' '<' + "Script_Completion_Percentage" + '>' + SC + '</' + "Script_Completion_Percentage" + '>'
print '     ' '<' + "Call_Completion_Percentage" + '>' + CC + '</' + "Call_Completion_Percentage" + '>'
print '     ' '<' + "call_attemps_per_sec" + '>' + call_attemps_per_sec + '</' + "call_attemps_per_sec" + '>'
print '     ' '<' + "Total_call_attempts" + '>' + Total_call_attempts + '</' + "Total_call_attempts" + '>'
print '     ' '<' + "Total_Script_attempts" + '>' + Total_Script_attempts + '</' + "Total_Script_attempts" + '>'
print ' ' "</" +script + "_Results>"
print "</ParsingResults>"