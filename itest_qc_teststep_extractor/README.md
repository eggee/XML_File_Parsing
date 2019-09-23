# itest_test-step_extractor
Extracts the (QC) test step information from an existing iTest test-case(s) (*.fftc files)
and writes it to an XML file. The XML file is the format that was chosen to be used when running pytest.
pytest will poing to the XML to get parameters and test-step information.

To run it, change the 'path' information to point to the local file "025G1_Cross.....fftc"

itest_file = "025G1_Cross-Slot_LAG_2x10Gig_to_Cisco.fftc"
#create a new *.xml file using the same name from the *.fftc new_file
file_name = itest_file.split('.')
file_name = file_name[0]
new_file = ('%s.xml' % file_name)

Run it:
>python itest_file_qc_extractor_and_xml_fileGen.py

The other files aren't necessary.

