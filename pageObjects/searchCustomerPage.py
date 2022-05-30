from selenium.webdriver.common.by import By


class searchCustomer:
    txt_email_id='SearchEmail'
    text_firstName_id='SearchFirstName'
    text_lastName_id='SearchLastName'
    btn_search_id='search-customers'

    tbl_searcResult_xpath='//*[@role="grid"]'
    tbl_xpath='//*[@id="customers-grid"]'
    table_rows_xpath='//*[@id="customers-grid"]/tbody/tr'
    table_col_xpath = '//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver=driver

    def setEmail(self,email):

        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID, self.text_firstName_id).clear()
        self.driver.find_element(By.ID, self.text_firstName_id).send_keys(firstname)

    def setLastname(self,lastname):
            self.driver.find_element(By.ID, self.text_lastName_id).clear()
            self.driver.find_element(By.ID, self.text_lastName_id).send_keys(lastname)

    def clickonSearch(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH ,self.table_rows_xpath))

    def getNoOfCols(self):
        return len(self.driver.find_elements(By.XPATH, self.table_col_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, self.tbl_xpath)
            emailid=table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[2]').text
            if emailid ==email:
                flag =True
                break
        return flag




    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.tbl_xpath)
            name = table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr[' + str(r) + ']/td[3]').text
            if name == Name:
                flag = True
                break
        return flag
