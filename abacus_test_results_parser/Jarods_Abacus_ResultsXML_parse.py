import sys
import os
import copy
import pprint

try:
    from lxml import etree, objectify
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


class StatParse:
    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath
        self.output = []  # output is a list that will contain dictionaries of dictionaries
        self.inner_dict = {}  # The inner_dict will hold the script-comments associated with their set numbers.
        self.extra_dict = {}  # extra_dict is used to gather the desired information together.
        self.outer_dict = {}  # The outer_dict will take in the extra_dict information and be appended to the output.

    def find(self):
        # Find the desired file.
        result = ''
        for root, dirs, files in os.walk(self.filepath):
            if self.filename in files:
                result = os.path.join(root, self.filename)
        return result

    def locate_2(self, root):
        # Used to iterate through the various
        # sets found in the .xml

        # This for loop iterates through all sets for the script-comments.
        # x will be used to acquire the set number.
        for x in root.xpath("/report/partition-and-timing-settings/set-list/set"):
            # e will be used to acquire the script-comment.
            for e in root.xpath("/report/partition-and-timing-settings/set-list/set[@num='%s']/set-scripts"
                                "/script-comments" % x.attrib['num']):
                # Example: '1' = 'GR303-N16S1A2c'
                self.inner_dict[x.attrib['num']] = e.text

        # Loops through the stat-channels using the set numbers with the inner_dict as a reference.
        for y in root.xpath("/report/channel-data/gen-stats/stat-channels"):
            # Serves as an error check to ensure proper functionality.
            if y.attrib['set'] in self.inner_dict.keys():
                # Find the desired data and add it to the extra_dict. The extra_dict information is added
                # to the outer_dict, and the extra_dict is then cleared for another go.
                for x in root.xpath("/report/channel-data/gen-stats/stat-channels[@set='%s']/stat-totals"
                                    "/total" % y.attrib['set']):
                    self.extra_dict['script-attempts'] = x.attrib['script-attempts']
                    self.extra_dict['percent-script-completions'] = x.attrib['percent-script-completions']
                    self.extra_dict['call-attempts'] = x.attrib['call-attempts']
                    self.extra_dict['call-attempts-per-sec'] = x.attrib['call-attempts-per-sec']
                    self.extra_dict['percent-call-completions'] = x.attrib['percent-call-completions']
                    self.extra_dict['errors'] = x.attrib['errors']
                    # Due to the nature of dictionaries, the copy function is necessary
                    # to ensure proper information transfer.
                    resource = copy.deepcopy(self.extra_dict)
                    self.outer_dict[self.inner_dict[y.attrib['set']]] = resource
                    # Clear the extra_dict after acquiring its information.
                    self.extra_dict.clear()
        self.output.append(self.outer_dict)

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

        # This is simply a pretty print variable
        # intended to make outputs more readable for the user.
        # pp = pprint.PrettyPrinter(indent=2)

        # Gathers the necessary data for the output
        self.locate_2(root)

        return self.output


if __name__ == '__main__':
    """

    """

    # Hard-coded name and path for development process.
    name = "BulkCall_SystemTest_780channels_Mgcp_Sip_and_GR303.xml"  # Disable if using name from argparse.
    # The path will search the topologies folder for the file.
    path = os.getcwd()

    # initiate an instance
    instance = StatParse(name, path)

    output = instance.parse()
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(output)
