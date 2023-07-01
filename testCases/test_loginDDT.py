import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutils
import time




class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/loginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******** Test_002_DDT_Login *********")
        self.logger.info("************ Verifying login test  ****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver) ###

        self.rows=XLutils.getRowCount(self.path,'Sheet1')
        print("number of rows in a Excel:",self.rows)

        lst_status=[]  #emppty list variable

        for r in range(2,self.rows+1):
            self.user=XLutils.readData(self.path,'Sheet1',r,1)
            self.password=XLutils.readData(self.path, 'Sheet1', r, 2)
            self.exp=XLutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("*****passed*******")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("*****failed********")
                    self.lp.clickLogout()
                    lst_status.append("fail")

            if act_title!=exp_title:
                if self.exp=="pass":
                    self.logger.info("*****failed****")
                    lst_status.append("fail")
                elif self.exp=="fail":
                    self.logger.info("*****passed*********")
                    lst_status.append("pass")
        if "fail" not in lst_status:
            self.logger.info("*****Login DDT test is passed******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********Login DDT test is failed*****")
            self.driver.close()
            assert False

        self.logger.info(" *****End of Login DDT Test*******")
        self.logger.info(" ********** Completed TC_loginDDT_002 *********")