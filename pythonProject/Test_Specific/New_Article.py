import time
import sys
sys.path.append(r"\pythonProject\Common")
import Helpers as H
from selenium.webdriver.common.keys import Keys
import Xml_Reader as Tst

def New_Article(driver, xml_dictionary, main_tag="NewArticle"):
    try:
        driver.implicitly_wait(30)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag='HomePageWebElements', sub_tag='btnNewArticle')).click()
        driver.implicitly_wait(30)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, sub_tag='txtArticletitle')).send_keys(H.Article_Title)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, sub_tag='txtArticleAbout')).send_keys(H.Article_about)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, sub_tag='txtWriteArticle')).send_keys(H.Article_Desc)
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, sub_tag='txtEntertags')).send_keys(H.Article_tags)
        driver.implicitly_wait(30)
        Publish_Article = driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary,main_tag,'btnPublishArticle'))
        Publish_Article.send_keys(Keys.ENTER)
    except Exception as e:
        print("Error ", e)