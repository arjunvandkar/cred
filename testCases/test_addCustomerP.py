import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.parametrize("customer_role, manager_of_vendor", [("Administrators", "Vendor 2"), ("Customers", "Vendor 3")])
    @pytest.mark.sanity
    def test_addCustomer(self, setup, customer_role, manager_of_vendor):
        self.logger.info("******** Test_003_AddCustomer  ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*******Login successful********")

        self.logger.info("****** Starting Add Customer Test ******")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("******* Providing Customer info  *******")

        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(8))
        self.email = random_string + "@gmail.com"
        self.addcust.setEmail(self.email)

        self.addcust.setPassword("test123")
        self.addcust.setCutomerRoles(customer_role)
        self.addcust.setManagerOfVendor(manager_of_vendor)
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Arjun")
        self.addcust.setLastName("Vandkar")
        self.addcust.setDob("7/05/1985")  # format d/mm/yyyy
        self.addcust.setCompanyname("Panasonic")
        self.addcust.setAdminConten("Automation Test Engineer")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving the customer info ********")

        self.logger.info("******** Add customer validation started  ********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("****** Add customer test passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_003.png")
            self.logger.error("********Add Customer test failed**********")
            assert True == False
        self.driver.close()

        self.logger.info("******** Test_003_AddCustomer completed **********")
