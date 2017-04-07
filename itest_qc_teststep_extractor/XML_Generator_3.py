from lxml import etree
from lxml.builder import ElementMaker  # lxml only !

E = ElementMaker(namespace="http://my.de/fault/namespace",
                 nsmap={'p': "http://my.de/fault/namespace"})

DOC = E.doc
TITLE = E.title
SECTION = E.section
PAR = E.par

my_doc = DOC(
    TITLE("The dog and the hog"),
    SECTION(
        TITLE("The dog"),
        PAR("Once upon a time, ..."),
        PAR("And then ...")
    ),
    SECTION(
        TITLE("The hog"),
        PAR("Sooner or later ...")
    )
)
print(etree.tostring(my_doc, pretty_print=True))
#print(etree.tostring(my_doc))