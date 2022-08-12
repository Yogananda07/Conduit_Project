#Project Imports
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append(r"\pythonProject\Common")
import Xml_Reader as Tst

def SignUpPage_Helper(driver, xml_dictionary ,username, email, password,main_tag="SignUpPageWebElements"):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,Tst.get_xpath_dictionary_for_pages(xml_dictionary,main_tag,'btnSignUpMainpage')))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, 'txtUserName')))).send_keys(username)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, 'txtEmail')))).send_keys(email)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, 'txtPassword')))).send_keys(password)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag, 'btnSignUp')))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, Tst.get_xpath_dictionary_for_pages(xml_dictionary, main_tag='HomePageWebElements', sub_tag='btnSettings'))))
    except Exception as e:
        print("Error ", e)

    #driver.find_element_by_xpath(Tst.get_xpath_dictionary_for_pages(xml_dictionary,main_tag,'btnSignUpMainpage')).click()





