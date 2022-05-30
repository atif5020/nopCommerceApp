import pytest

from pageObjects.addCustomerPage import addCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.searchCustomerPage import searchCustomer
from utilities.customLogger import logGen
from utilities.readProperties import ReadConfig

class  Test_004_searchCustomerByEmail:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()
    logger = logGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setUp):
        self.logger.info("**************Test_004_searchCustomerByEmail*********************")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login done*******")

        self.logger.info("**************search page opening*******")

        self.addcust = addCustomer(self.driver)  # to access all action methods in PageObject Class of addCustomerPage
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("***********starting search customer by email**********")

        self.searchCust = searchCustomer(self.driver)
        self.searchCust.setEmail('victoria_victoria@nopCommerce.com')
        self.searchCust.clickonSearch()
        status=self.searchCust.searchCustomerByEmail('victoria_victoria@nopCommerce.com')
        assert True == status
        self.logger.info("**************search by email completed*******")
        self.driver.close()
