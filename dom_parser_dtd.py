from lxml import etree
import xml.etree.ElementTree as ET

schema_path = "./schema.xml"
xml_file_path = "./data.xml"

xml_schema_doc = etree.parse(schema_path)

xml_schema = etree.XMLSchema(xml_schema_doc)

xml_doc  = etree.parse(xml_file_path)
# raise an error is xml does not match schema
xml_schema.assert_(xml_doc)

#returns true if the xml matches the schema
result = xml_schema.validate(xml_doc )

print(result)

# iterate over all children and grandchildren of the root element and print corresponding text
for child in xml_doc.getroot():
    print(child.tag," : ", child.text)
    for grandchild in child:
        print(grandchild.tag ," : ", grandchild.text)