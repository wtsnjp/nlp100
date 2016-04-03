import sys
from xml.etree import ElementTree as ET

file_name = sys.argv[1]

tree = ET.parse(file_name)
root = tree.getroot()
words = root.findall(".//word")

for w in words:
    print(w.text)
