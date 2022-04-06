import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action= "store", default="chrome", help= "type in browser name")

@pytest.fixture(scope="class")
def test_setup(request):
    s = Service("C:/Users/RUKMINI/PycharmProjects/SeleniumPythonFramework1/drivers/chromedriver.exe")
    s1 = Service("C:/Users/RUKMINI/PycharmProjects/SeleniumPythonFramework1/drivers/geckodriver.exe")
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(service=s)
    elif browser == 'firefox':
        driver = webdriver.firefox(service=s1)
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("test completed")