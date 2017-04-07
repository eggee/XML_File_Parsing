from lxml import etree
from lxml.builder import E as buildE

class DummyCursor(object):
  def __init__(self,fields,rows=5):
    self.description = [[f] for f in fields]
    self.data = [ ["%s%02d" % (f,i) for f in fields] for i in range(rows) ]
  def fetchall(self):
    return self.data

def E(tag,parent=None,content=None):
  """Simple E helper"""
  element = buildE(tag)
  if content is not None:
    element.text = unicode(content)
  if parent is not None:
    parent.append(element)
  return element

def fetchXML(cursor):
  fields = [x[0] for x in cursor.description ]
  doc = E('data')
  for record in cursor.fetchall():
    r = E('row',parent=doc)
    for (k,v) in zip(fields,record):
      E(k,content=v,parent=r)
  return doc

doc = fetchXML(DummyCursor(['name','description']))

print etree.tostring(doc,pretty_print=True)