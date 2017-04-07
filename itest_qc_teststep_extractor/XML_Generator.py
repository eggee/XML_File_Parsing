from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import pprint

root = Element('person')
tree=ElementTree(root)  # <person />
name = Element('name')
name.text = 'Julie'
root.append(name)
# root.set('id', '123')

print etree.tostring(root)
#pprint.pprint(etree.tostring(root))
#print etree.tostring(root)
#print root()
tree.write(open('person.xml', 'wb'))
