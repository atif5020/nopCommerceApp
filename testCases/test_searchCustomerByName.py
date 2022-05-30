import pytest

from pageObjects.addCustomerPage import addCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.searchCustomerPage import searchCustomer
from utilities.customLogger import logGen
from utilities.readProperties import ReadConfig


class Test_005_searchCustomerByName:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()
    logger = logGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setUp):
        self.logger.info("**************Test_005_searchCustomerByName*********************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login done*******")

        self.addcust = addCustomer(self.driver)  # to access all action methods in PageObject Class of addCustomerPage
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.logger.info("**************search page opened*******")

        self.logger.info("***********starting search customer by Name**********")

        self.searchCust = searchCustomer(self.driver)
        self.searchCust.setFirstname('Victoria')
        self.searchCust.setLastname('Terces')
        self.searchCust.clickonSearch()
        status = self.searchCust.searchCustomerByName('Victoria Terces')
        assert True == status
        self.logger.info("**************search by Name completed*******")
        self.driver.close()
