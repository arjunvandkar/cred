import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
        # add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//i[@class='nav-icon far fa-dot-circle']"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"

    txtFirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_Xpath = "//input[@id='LastName']"


    rdMaleGender_xpath = "//label[@for='Gender_Male']"
    rdFeMaleGender_xpath = "//label[@for='Gender_Female']"


    txt_DOB_xpath = "//input[@id='LastName']"
    txt_CompanyName_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"

    lstitemAdministrators_xpath="//section[@class='content']//li[1]"
    lstitemRegistered_xpath="//span[normalize-space()='Registered']"
    lstitemGuest_xpath="//span[normalize-space()='Guests']"
    lstitemVendors_xpath="//span[normalize-space()='Vendors']"
    lstitemForum_Moderators_xpath="//span[normalize-space()='Forum Moderators']"

    drpmgrofvendor = "//select[@id='VendorId']"

    txt_AdminContent_xpath="//textarea[@id='AdminComment']"
    btn_Save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCutomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrofvendor))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif gender=="female":
            self.driver.find_element(By.XPATH,self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txt_LastName_Xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setCompanyname(self,comname):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(comname)

    def setAdminConten(self,content):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()

