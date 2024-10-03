#!/usr/bin/python3
"""Defines a function to convert XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    "serialize a dictionary to a file."
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserializes an XML file to python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
