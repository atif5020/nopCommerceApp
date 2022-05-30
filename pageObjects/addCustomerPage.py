from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class addCustomer:
    linkcustomer_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    linkcustomer_menuItem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_addnew_xpath = '/html/body/div[3]/div[1]/form[1]/div/div/a'
    txt_email_xpath = '//*[@id="Email"]'
    txt_password_xpath = '//*[@id="Password"]'
    txt_firstname_xpath = '//*[@id="FirstName"]'
    txt_lastname_xpath = '//*[@id="LastName"]'
    radio_male_id = "Gender_Male"
    radio_female_id = "Gender_Female"
    txt_dob_xpath = '//*[@id="DateOfBirth"]'
    txt_companyname_xpath = '//*[@id="Company"]'
    txt_customerrole_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    listitem_administrators_xpath = '//li[contains(text(),"Administrators")]'
    listitem_registered_xpath = '//li[contains(text(),"Registered")]'
    listitem_guests_xpath = '//li[contains(text(),"Guests")]'
    listitem_vendors_xpath = '//li[contains(text(),"Vendors")]'
    listitem_forummoderators_xpath = 'Forum Moderators'
    drp_managerofvendor_xpath = '//*[@id="VendorId"]'
    txt_admcomment_xpath = '//*[@id="AdminComment"]'
    btn_save_xpath = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]'


    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkcustomer_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkcustomer_menuItem_xpath).click()

    def clickonAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
            self.driver.find_element(By.XPATH, self.txt_lastname_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender == "male":
            self.driver.find_element(By.ID, self.radio_male_id).click()
        elif gender == "female":
            self.driver.find_element(By.ID, self.radio_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_male_id).click()

    def setDob(self,dob):
            self.driver.find_element(By.XPATH, self.txt_dob_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
            self.driver.find_element(By.XPATH, self.txt_companyname_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_companyname_xpath).send_keys(companyname)

    def setCustomerRoles(self,role):
            self.driver.find_element(By.XPATH, self.txt_customerrole_xpath).click()
            if role=="Registered":
                self.listitem=self.driver.find_element(By.XPATH, self.listitem_registered_xpath)
            elif role=="Administrators":
                self.listitem=self.driver.find_element(By.XPATH, self.listitem_administrators_xpath)
            elif role=="Guests":
                self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
                self.listitem = self.driver.find_element(By.XPATH, self.listitem_guests_xpath)
            elif role == "Forum Moderators":
                self.listitem = self.driver.find_element(By.XPATH, self.listitem_forummoderators_xpath)
            elif role == "Vendors":
                self.listitem = self.driver.find_element(By.XPATH, self.listitem_vendors_xpath)
            else:
                self.listitem = self.driver.find_element(By.XPATH, self.listitem_guests_xpath)
            self.driver.execute_script("arguments[0].click();", self.listitem)  # this is javascript, to click on item

    def setManagerofVendor(self,value):
            drp=Select(self.driver.find_element(By.XPATH, self.drp_managerofvendor_xpath))
            drp.select_by_visible_text(value)

    def setAdminComment(self,comment):
            self.driver.find_element(By.XPATH, self.txt_dob_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_admcomment_xpath).send_keys(comment)

    def clickonSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()









