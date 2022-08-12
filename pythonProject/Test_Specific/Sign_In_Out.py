import time
import sys
sys.path.append(r"\pythonProject\Common")
import Helpers as H, Xml_Reader as Tst
from selenium.webdriver.common.keys import Keys

def SignIn_Helper(driver, xml_dictionary, main_tag="SignIn"):
    try:
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag='HomePageWebElements', sub_tag='btnSignInHP')).click()
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary,main_tag,'txtUserName')).send_keys(H.SignUpcheck(False))
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary,main_tag,'txtPassword')).send_keys('password')
        Signin_button = driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, 'btnSignIn'))
        Signin_button.send_keys(Keys.ENTER)
    except Exception as e:
        print("Error ", e)


def SignOut_Helper(driver, xml_dictionary, main_tag="SettingsPage"):
    try:
        driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag='HomePageWebElements', sub_tag='btnSettings')).click()
     #  driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary, 'btnSettings', main_tag='HomePageWebElements')).click()
        logout_button = driver.find_element("xpath",Tst.get_xpath_dictionary_for_pages(xml_dictionary,main_tag,'btnLogout'))
        logout_button.send_keys(Keys.ENTER)
    except Exception as e:
        print("Error ", e)

    # logout_button.click()
