import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_Login:
    baseURL = ReadConfig.getAppUrl()  # baseURL = "https://admin-demo.nopcommerce.com/"
    username = ReadConfig.getUserName()  # username = "admin@yourstore.com"
    password = ReadConfig.getUserPassword()  # password = "admin"

    logger = logGen.loggen()

    @pytest.mark.sanity  # groupng marker
    @pytest.mark.regression  # groupng marker
    def test_homePageTitle(self, setUp):

        self.logger.info("********************* Test_001_Login ******************")
        self.logger.info("************ Verifying Home page Title ****************")

        self.driver = setUp  # contest.py used here
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home page Title test is passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************ Home page Title test is failed ****************")
            assert False

    @pytest.mark.regression  # grouping marker
    def test_login(self, setUp):
        self.logger.info("************ Verifying Home page Title ****************")
        self.driver = setUp  # contest,py used here
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # now we need to create object of LoginPage class of 'pageObjects'
        # in that class, a constructor expects a driver so we will pass here 'sel.driver'
        self.lp = LoginPage(self.driver)  # created object and stored in a variable 'lp'
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************ Login test is passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("************ Login test is failed ****************")
            assert False
