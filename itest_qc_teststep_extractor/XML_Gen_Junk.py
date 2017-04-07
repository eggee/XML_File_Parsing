from lxml import etree
from xml.etree.ElementTree import ElementTree

root = etree.Element("root")

print root.tag

root.append(etree.Element("child1"))

child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

xml_tree = etree.tostring(root, pretty_print=True)
print xml_tree
#xml_tree.write(open('xml_tree.xml', 'wb'))