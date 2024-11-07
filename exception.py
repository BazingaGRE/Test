from lxml import etree

article_date_count = dict()

def yearly_articles(elem):
    if elem.tag == "year":
        if elem.text in article_date_count:
            article_date_count[elem.text] += 1
        else:
            article_date_count[elem.text] = 1

def preprocess_xml(xml_file):
    # Read the XML file and preprocess it
    with open(xml_file, 'r', encoding='ISO-8859-1') as f:
        xml_content = f.read()

    # Replace undefined entities with their corresponding characters
    xml_content = xml_content.replace('&auml;', 'ä')  # Add more replacements as needed
    # Add more entity replacements as needed

    return xml_content

def parse_xml(xml_file):
    # Preprocess the XML content
    xml_content = preprocess_xml(xml_file)

    # Parse the corrected XML content
    parser = etree.XMLParser(recover=True)  # Allow recovery from minor issues
    root = etree.fromstring(xml_content.encode('ISO-8859-1'), parser)

    for elem in root.iter('year'):
        yearly_articles(elem)

# Replace with your XML file path
parse_xml('dblp-2024-10-01.xml')
print(article_date_count)