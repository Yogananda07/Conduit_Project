import json
import xmltodict

def get_xml_dictionary():
    with open(r"C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Common\Object_Rep.xml", "r") as fd:
        codes = xmltodict.parse(fd.read())
    return codes

def get_xpath_dictionary_for_pages(dict_obj,main_tag,sub_tag):
    return dict_obj['QUREAI'][main_tag][sub_tag]




