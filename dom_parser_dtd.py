from lxml import etree
import xml.etree.ElementTree as ET

# parser = etree.XMLParser(dtd_validation=True)

schema_path = "./schema.xml"
xml_file_path = "./data.xml"

xml_schema_doc = etree.parse(schema_path)

xml_schema = etree.XMLSchema(xml_schema_doc)

xml_doc  = etree.parse(xml_file_path)

# result = xml_schema.validate(xml_doc )
# xml_schema.assert_(xml_doc)
# print(result)
print(xml_doc.getroot())

for child in xml_doc.getroot():
    print(child.tag, child.attrib)