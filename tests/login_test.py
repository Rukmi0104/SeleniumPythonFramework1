import allure
import moment
from selenium import webdriver
import pytest
from pages.homePage import Homepage
from pages.loginPage import LoginPage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        try:
            x = driver.title
            assert x == "abc"
            print(x)
        except AssertionError as error:
            print("assertion error occurred")
            print(error)
            currentTime = moment.now().strftime("%D-%M-%y_%H-%M-%S")
            Test_name= utils.whoami()
            screenshot = Test_name + "_" + currentTime
            allure.attatch(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type = allure.attachment_type.PNG)
            raise

        except:
            print("there was an error")
            currentTime = moment.now().strftime("%D-%M-%y_%H-%M-%S")
            Test_name = utils.whoami()
            screenshotname = Test_name + "_" + currentTime
            allure.attatch(self.driver.get_screenshot_as_png(), name=screenshotname,
                           attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/RUKMINI/PycharmProjects/SeleniumPythonFramework1/screenshots" + screenshotname + ".png")


        else:
            print("No exception occurred")

        finally:
            print("Finally block will always execute")


#C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1>
# python -m pytest C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests\login_test.py --html=report/report.html #

#C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1>
# python -m pytest C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests\login_test.py --html=report/report1.html --self-contained-html


#for pytest_addoption
#C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests>
# python -m pytest C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests\login_test.py --browser chrome

#allure reports commands
#command 1:
# C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests>
# python -m pytest C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests\login_test.py --alluredir=C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\report\allure-reports

#command 2:
#C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\tests>
# allure serve C:\Users\RUKMINI\PycharmProjects\SeleniumPythonFramework1\report\allure-reports

