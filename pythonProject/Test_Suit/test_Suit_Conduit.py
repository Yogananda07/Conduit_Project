import sys
sys.path.append(r"\pythonProject\Test_Specific")
sys.path.append(r"\pythonProject\Common")
from selenium import webdriver
import Cmt_Fav as CF
import New_Article as NA, Sign_In_Out as SO, Sign_Up as SU
import Xml_Reader as Tst, Helpers as H

log_file_path_SignUp = r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Logs\SignupLog.txt'
log_file_path_SignIn_SignOut = r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Logs\SignIn_SignUpLog.txt'
log_file_New_Article = r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Logs\New_ArticleLog.txt'
#Onstart

def test_Conduit_SignUp():
    driver = webdriver.Chrome(H.executable_path)
    H.Launch_Browser(driver)
    global_dict_obj = Tst.get_xml_dictionary()
    try:
        SU.SignUpPage_Helper(driver, global_dict_obj, H.username, H.SignUpcheck(True), "password")
        SO.SignOut_Helper(driver, global_dict_obj)
    except Exception as e:
        print("Conduit User SignUp failed.")
        H.take_screenshot(driver, "test_Conduit_SignUp")
        H.print_trackback_and_quit_browser(driver)
        assert SU.SignUpPage_Helper()
        print("Error ", e)

    finally:
        H.print_trackback_and_quit_browser(driver,log_file_path_SignUp)


def test_Conduit_SignInSignOut():
    driver = webdriver.Chrome(H.executable_path)
    H.Launch_Browser(driver)
    global_dict_obj = Tst.get_xml_dictionary()
    try:
       SO.SignIn_Helper(driver,global_dict_obj)
       SO.SignOut_Helper(driver, global_dict_obj)
    except Exception as e:
        print("Conduit SignIn/SignOut failed.")
        H.take_screenshot(driver, "test_Conduit_SignIn_SignOut")
        H.print_trackback_and_quit_browser(driver)
        print("Error ", e)

    finally:
        H.print_trackback_and_quit_browser(driver,log_file_path_SignIn_SignOut)
def test_Conduit_New_Article():
    driver = webdriver.Chrome(H.executable_path)
    H.Launch_Browser(driver)
    global_dict_obj = Tst.get_xml_dictionary()
    try:
        SO.SignIn_Helper(driver, global_dict_obj)
        NA.New_Article(driver,global_dict_obj)
        SO.SignOut_Helper(driver, global_dict_obj)
    except Exception as e:
        print("Conduit New Article creation failed.")
        H.take_screenshot(driver, "test_Conduit_New_Article")
        H.print_trackback_and_quit_browser(driver)
        print("Error ", e)
    finally:
        H.print_trackback_and_quit_browser(driver,log_file_New_Article)
def test_Comment_favorite():
    driver = webdriver.Chrome(H.executable_path)
    H.Launch_Browser(driver)
    global_dict_obj = Tst.get_xml_dictionary()
    try:
        SO.SignIn_Helper(driver, global_dict_obj)
        CF.Comment_Article(driver,global_dict_obj)
        SO.SignOut_Helper(driver, global_dict_obj)
    except Exception as e:
        print("Conduit commenting and favorite is failed.")
        H.take_screenshot(driver, "test_Comment_favorite")
        H.print_trackback_and_quit_browser(driver)
        print("Error ", e)
    finally:
        H.print_trackback_and_quit_browser(driver,log_file_New_Article)
#Onfinish