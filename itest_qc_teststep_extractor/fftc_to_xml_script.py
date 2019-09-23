import sys
import os
import pprint

try:
    from lxml import etree, objectify, builder
except ImportError:
    print "Failed to import lxml.etree!!!\n" \
          "Terminating script.\n" \
          "Please install lxml for Python 2.7.\n" \
          "Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml\n" \
          "Download lxml-3.7.2-cp27-cp27m-win_amd64.whl\n" \
          "Go to the directory now containing the file and\n" \
          "use 'pip install lxml-3.7.2-cp27-cp27m-win_amd64.whl'\n" \
          "from the command prompt."
    sys.exit()


class FftcToXml:
    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath

    def find(self):
        # Find the desired file.
        result = ''
        for root, dirs, files in os.walk(self.filepath):
            if self.filename in files:
                result = os.path.join(root, self.filename)
        return result

    def parse(self):
        fileFound = self.find()
        # Print out the file name once found.
        # This serves as an error check check for the user as well.
        # print
        # print "File location: " + fileFound
        # print

        # Attempt to open the file.
        # If file could not be opened, terminate the script early.
        try:
            XMLfile = open(fileFound, "r+")  # Read+Write.
        except IOError:
            print "Could not open file!\n" \
                  "Terminating script.\n" \
                  "Make sure the name and path arguments are correct."
            sys.exit()

        # Parse the XMLfile.
        # Set root to the root of tree.
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(XMLfile, parser)
        root = tree.getroot()
        # Not sure how it works, but this block takes care of
        # the namespaces.
        for elem in root.getiterator():
            if not hasattr(elem.tag, 'find'):
                continue  # (1)
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i + 1:]
        objectify.deannotate(root, cleanup_namespaces=True)

        # Open the file to write to, or create a new file if not already created.
        file_to_write = open('yay.xml', 'wb')

        # Write in the xml version and encoding.
        file_to_write.write('<?xml version="1.0" encoding="UTF-8"?>\n')

        # Declare elements that will make up the tree.
        script_file = etree.Element('script_file')
        qc_steps = etree.SubElement(script_file, 'qc_steps')

        # Track step names to prevent duplicate processing.
        stepnamelist = []

        # Track number of steps in the xml.
        num = 1

        # Boolean flag to watch for duplicate steps.
        duplicate_step_found = False
        for qualityCenterStepInfo in root.iter("qualityCenterStepInfo"):
            # Use try statements to ensure data is present.
            try:
                stepname = qualityCenterStepInfo.get('stepName')
                # If duplicate is found, set flag accordingly.
                if stepname in stepnamelist:
                    duplicate_step_found = True
                # Add stepname to stepnamelist for later reference in case of duplicates.
                stepnamelist.append(stepname)
            except AttributeError:
                stepname = "BLANK"
            # Runs only if current step is not a duplicate.
            if not duplicate_step_found:
                try:
                    description = qualityCenterStepInfo.find("description").text
                except AttributeError:
                    description = "BLANK"
                try:
                    expected_result = qualityCenterStepInfo.find("expectedResult").text
                except AttributeError:
                    expected_result = "BLANK"
                # Builds a Step in the etree.
                Step = etree.SubElement(qc_steps, 'Step')
                etree.SubElement(Step, 'step', name='Number').text = str(num)
                etree.SubElement(Step, 'step', name='Name').text = stepname
                etree.SubElement(Step, 'step', name='Description').text = description
                etree.SubElement(Step, 'step', name='Expected').text = expected_result
                # Increment num to represent number of steps.
                num += 1
            else:
                # Reset flag.
                duplicate_step_found = False

        # Write the xml file.
        XMLwriter = etree.ElementTree(script_file)
        file_to_write.write(etree.tostring(XMLwriter, pretty_print=True))

        # Print statement.
        # print(etree.tostring(XMLwriter, pretty_print=True))

        return


if __name__ == '__main__':
     # Hard-coded name and path for development process.
    name = "n16s1-GR303-A2Combo-BulkCall-via-SM025Gx.fftc"  # Disable if using name from argparse.
    # The path will search the topologies folder for the file.
    path = os.getcwd()

    # initiate a CLASS instance
    instance = FftcToXml(name, path)
    instance.parse()
