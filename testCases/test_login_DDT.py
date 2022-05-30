import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getAppUrl()  # baseURL = "https://admin-demo.nopcommerce.com/"
    path = ".\\TestData\\LoginData.xlsx"

    logger = logGen.loggen()

    @pytest.mark.regression  # grouping marker
    def test_login_DDT(self, setUp):
        self.logger.info("********************* Test_0012_DDT_Login ******************")
        self.logger.info("************ Verifying Login DDT  ****************")
        self.driver = setUp  # contest,py used here
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # now we need to create object of LoginPage class of 'pageObjects'
        # in that class, a constructor expects a driver, so we will pass here 'self.driver'
        self.lp = LoginPage(self.driver)  # created object and stored in a variable 'lp'

        # to get data from xl file
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("number of rows in excel file:", self.rows)

        list_status=[] # empty list variable
        for r in range(2,self.rows+1):
            self.username=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expected_status = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            act_title = self.driver.title

            if act_title == "Dashboard / nopCommerce administration":
                if self.expected_status == "pass":
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout()
                    list_status.append("pass")
                elif self.expected_status == "fail":
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout()
                    list_status.append("fail")
            elif act_title != "Dashboard / nopCommerce administration":
                if self.expected_status == "pass":
                    self.logger.info("**** failed ****")
                    list_status.append("fail")
                elif self.expected_status == "fail":
                    self.logger.info("**** passed ****")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("******** Login DDT is passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******** Login DDT is failed *********")
            self.driver.close()
            assert False

        self.logger.info("************ End of DDT test ****************")
        self.logger.info("************ Completed Test_0012_DDT_Login  ****************")

