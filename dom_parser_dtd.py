from lxml import etree

# paths to files
schema_path = "./schema.xml"
xml_file_path = "./data.xml"
dtd_file_path = "./dtd.dtd"

# lxml objects
xml_schema_doc = etree.parse(schema_path)
xml_schema = etree.XMLSchema(xml_schema_doc)
xml_doc  = etree.parse(xml_file_path)
dtd = etree.DTD(dtd_file_path)

# raise an error is xml does not match schema
xml_schema.assert_(xml_doc)

#validate returns true if the xml matches the schema in the schema file
schema_result = xml_schema.validate(xml_doc)
print("xml matches the schema: ", schema_result)

# raise an error is xml does not match dtd
dtd.assert_(xml_doc)

#validate returns true if the xml matches the dtd in the dtd file
dtd_result = dtd.validate(xml_doc)
print("xml matches the dtd file: ", dtd_result)

# iterate over all children and grandchildren of the root element and print corresponding text
# for child in xml_doc.getroot():
#     for grandchild in child:
#         print(grandchild.tag ," : ", grandchild.text)
#     print("\n")
