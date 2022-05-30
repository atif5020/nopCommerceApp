from selenium import webdriver
from selenium.webdriver.common.by import By


# In this way we design page object class:

class LoginPage:
    # =========================================================================================================
    # first: find all locators and store them in a variable
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = '//button[@class="button-1 login-button"]'
    link_logout_linktext = "Logout"

    # =========================================================================================================

    # --------------------------------------------------------------------------------------------
    # constructor:
    # to initialize driver at time of object creation we need to create constructor
    def __init__(self, driver):  # it wil capture driver from testcase
        self.driver = driver  # and it will initialize the local class variable(self.driver) which we will use here

    # ---------------------------------------------------------------------------------------------

    # =======================================================================================================
    # second: create action methods for all locators:
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    # ===================================================================================================

# next:
# now we will create our test case in testCase package
