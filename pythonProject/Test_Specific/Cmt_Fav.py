import time
import sys
sys.path.append(r"C:/Users/320042272.CODE1/PycharmProjects/pythonProject/Common")
import Helpers as H
import Xml_Reader as Tst
from selenium.webdriver.common.keys import Keys

def Comment_Article(driver, xml_dictionary, main_tag="GlobalFeed"):
    try:
        time.sleep(5)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag='HomePageWebElements', sub_tag='btnHome')).click()
        time.sleep(5)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag='HomePageWebElements', sub_tag='btnGlobalFeed')).click()
        items = driver.find_elements_by_tag_name("article-preview")
        for item in items:
            text = item.text
            if 'Create ' in item.text:
                print(text)
                item.find_elements_by_tag_name("a")[-1].click()
                break
        txt_fav = driver.find_element("xpath", Tst.get_xpath_dictionary_for_pages(global_dict_obj, main_tag,sub_tag='btnFavourite')).text
        print(txt_fav)
        if txt_fav == "Favorite Article":
            driver.find_element("xpath", Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag,sub_tag='btnFavourite')).click()
        driver.find_element("xpath", Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag,sub_tag='txtWriteComment')).send_keys(H.Article_Comment)
        driver.find_element("xpath", Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag,sub_tag='btnPostComment')).click()
    except Exception as e:
        print("Error ", e)
