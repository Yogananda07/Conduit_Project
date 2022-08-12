import random
import time
import traceback
from datetime import datetime

log_file_path = r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Logs\Log.txt'
num = random.randint(1010, 9999)

username = "Test"+str(num)

def SignUpcheck(Signup):
    if Signup == True:
        email1 = "Yo"+str(num)+"@gmail.com"
        with open(r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Common\UserCredentials.txt', 'w') as UCW:
            UCW.write(email1)
        return email1
    if Signup == False:
        with open(r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Common\UserCredentials.txt', 'r') as UCR:
            email1=UCR.readlines()
        return email1

executable_path="C:\Temp\chromedriver.exe"

Article_Title = "hello"
Article_about = "subject"
Article_Desc = "Description about article"
Article_tags = "tags"
Article_Comment = "Good one"

def Launch_Browser(driver):
    driver.get("https://demo.realworld.io/#/")
    driver.implicitly_wait(30)
    driver.maximize_window()

def take_screenshot(driver, testcasename):
    CurrDt = testcasename+'_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file(r'C:\Users\320042272.CODE1\PycharmProjects\pythonProject\Logs\%s.png' % CurrDt)

def print_trackback_and_quit_browser(driver,log_file_path):
    with open(log_file_path, "a") as f:
        f.write(str(traceback.format_exc()))
    driver.quit()
