import sys
import xml.etree.ElementTree

from xml.dom import minidom
from xml.sax import saxutils, make_parser

class ListHandler(saxutils.XMLGenerator):

    def __init__(self):
        super().__init__()

    def startElement(self, name, attrs):
        print ('start', name)   
        for attr_name, value in attrs.items():
            print (attr_name, value)

    def endElement(self, name):
        print ('end', name)

    def characters(self, content): 
        print (content)


if __name__ == '__main__':        
    #Parsowaniue uzywajac SAX 
    print("***Parsing using SAX***\n")
    parser = make_parser()
    parser.setContentHandler(ListHandler())
    parser.parse(sys.argv[1])
    
    #Parsowanie uzywajac DOM
    print("\n***Parsing using DOM***")
    doc = minidom.parse(sys.argv[1]) 
    items = doc.getElementsByTagName('address')

    for item in items:
        print(item.getAttribute("type"))
        print(item.firstChild.data)

    #Zmiana jednego elementu "podpisu" przy uzyciu Element Tree
    et = xml.etree.ElementTree.parse(sys.argv[1])
    root = et.getroot()

    for sign in root.findall('signature'):
        sign.text = str("Jakub King")
        sign.set('updated','yes')
    
    et.write(sys.argv[1])