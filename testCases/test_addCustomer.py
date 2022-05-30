import random
import string

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import addCustomer
from utilities.customLogger import logGen
from utilities.readProperties import ReadConfig
from selenium import webdriver





class  Test_003_addCustomer:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setUp):
        self.logger.info("**************Test_003_addCustomer*********************")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver) # to access all action methods in PageObject Class of LoginPage
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login done*******")

        self.logger.info("**************starting adding new customer*******")

        self.addcust=addCustomer(self.driver) # to access all action methods in PageObject Class of addCustomerPage
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.addcust.clickonAddNew()

        self.logger.info("**************providing info of new customer*******")

        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('12345')
        self.addcust.setFirstname('ali')
        self.addcust.setLastname('ahmed')
        self.addcust.setGender('male')
        self.addcust.setDob('12/02/1995')
        self.addcust.setCompanyName('abcxyz')
        self.addcust.setCustomerRoles('Guests')
        self.addcust.setManagerofVendor('Vendor 2')
        self.addcust.setAdminComment('ok ok ok')
        self.addcust.clickonSave()
        self.logger.info("************** saving customer info ************")

        self.logger.info("************** customer validation started *****")
        self.msg=self.driver.find_element(By.TAG_NAME,'body').text
        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("****************** Add customer test passed***************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("****************** Add customer test failed***************************")
            assert True ==False
        self.driver.close()
        self.logger.info("**************Completed Test_003_addCustomer*********************")





# to generate random emails
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
