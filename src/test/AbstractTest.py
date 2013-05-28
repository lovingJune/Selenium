'''
Created on Dec 13, 2012

@author: tinh.do
'''
import unittest
import HTMLTestRunner
import time
from config.Config import *
from config.DataReader import DataReader
import os
from page.AbstractPage import AbstractPage
from page.PageFactory import *
from reportlog.Log import Log
from reportlog.XMLToExcelReport import XMLToExcelReport
from browser.Browser import Browser
from xmlrunner import XMLTestRunner
#from report.XMLToExcelReport import XMLToExcelReport
from config.DataConfig import DataConfig
import time,sys
#from data.Config import HubNode, BrowserNoneGrid

class AbstractTest():
        
    dataset = None
    @classmethod
    def dataSet(cls):
        return cls.dataset
    
    def __init__(self):
        self.loginPage = None
        self.homePage = None
        
        # Read common test data
        self.dataReader("AbstractTest")
        self.home_url = AbstractTest.dataset.home_url
        self.facebook_url = AbstractTest.dataset.facebook_url
        self.twitter_url = AbstractTest.dataset.twitter_url         
        self.usernameFB = AbstractTest.dataset.usernameFB
        self.passwordFB = AbstractTest.dataset.passwordFB
        self.firstNameFB = AbstractTest.dataset.firstnameFB
        self.lastNameFB = AbstractTest.dataset.lastnameFB
        self.emailFB = AbstractTest.dataset.emailFB
        
        self.usernameTW = AbstractTest.dataset.usernameTW
        self.passwordTW = AbstractTest.dataset.passwordTW
        self.firstNameTW = AbstractTest.dataset.firstnameTW
        self.lastNameTW = AbstractTest.dataset.lastnameTW
        self.emailTW = AbstractTest.dataset.emailTW
        
        self.link_signintw_xpath = "//a[@class='tw-connect']"
        self.link_signinfb_xpath = "//a[@class='fb-connect']"
        self.btn_signouttw_id = "signout-button"
        self.lnk_signoutfb_xpath = "//input[@value='Log Out']"
        self.dropdown_usertw_id = "user-dropdown-toggle"
             
    '''
    Des: Verify expected result is True
    Arguments:
        expected: expected result (True/False)
        msg: Passed message
    '''
    # Verify True               
    def verifyTrue(self, expected, msg=None):
        self.assertTrue(expected)
        Log.logPass(msg)
    
    '''
    Des: Verify expected result is False
    Arguments:
        expected: expected result (True/False)
        msg: Passed message
    '''
    # Verify False
    def verifyFalse(self, expected, msg=None):
        self.assertFalse(expected) 
        Log.logPass(msg)  
    
    '''
    Des: Verify expected result equal with actual result
    Arguments:
        expectValue: expected result
        actualValue: actual result
        msg: Passed message
    '''   
    # Verify 2 String are same 
    def verifyEqual(self, expectValue, actualValue, msg="Expect value equal with actual value!"):
        self.assertEqual(expectValue, actualValue)
        Log.logPass(msg)
    
    '''
    Des: Verify expected result differ from actual result
    Arguments:
        expectValue: expected result
        actualValue: actual result
        msg: Passed message
    '''
    # Verify 2 String are not same
    def verifyNotEqual(self, expectValue, actualValue, msg="Expect value differ from actual value!"):
        self.assertNotEqual(expectValue, actualValue)
        Log.logPass(msg)
     
    # Read test data from xml file          
    def dataReader(self, test_module_name): 
        try:        
            env = os.getenv("PYTHONPATH_KLOUT")
            dataReader = DataReader(str(env) + "/config/testdata.xml").DataSet
            for node in dataReader.testmodule:
                if node.name == test_module_name:
                    AbstractTest.dataset = node
                    break
        except Exception, e:
            Log.logError(str(e))
      
    # Login Klout                      
    def login(self, alreadyExistedLoginPage=False, username=None, password=None, connectType="facebook"):
        try:
            self.loginPage = PageFactory.getLoginPage()
    
            if alreadyExistedLoginPage == False:
                AbstractPage.navigateToWeb(self.home_url)            
            
            # Login
            if username == None and password == None:
                username = self.username
                password = self.password
                    
            self.homePage = self.loginPage.loginKlout(username, password, connectType)
            
            return self.homePage
        except Exception, e:
            Log.logError(str(e))
    
    # Navigate to Klout
    def navigateToKlout(self):
        AbstractPage.navigateToWeb(self.home_url)
        
    # avigate to Twitter
    def navigateToTwitter(self):
        AbstractPage.navigateToWeb(self.twitter_url)
    
    # Login Klout by clicking at dropdown
    def loginBy_DropMenu(self, alreadyExistedAccount=False, username= None, password=None, connectType="facebook"):
        try:
            self.loginPage = PageFactory.getLoginPage()
    
            if alreadyExistedAccount == False:
                AbstractPage.navigateToWeb(self.home_url)
            else:
                AbstractPage.logoutKlout()
            
            # Login
            if username == None and password == None:
                username = self.username
                password = self.password
                
            self.homePage = self.loginPage.loginKlout_dropmenu(username, password, connectType)
            
            return self.homePage
        except Exception, e:
            Log.logError(str(e))
        
    # Login Facebook
    def loginFacebook(self, username, password, alreadyExistedAccount=False):
        try:
            self.loginPageFacebook = PageFactory.getFacebookLoginPage()
            
            if alreadyExistedAccount == False:
                AbstractPage.navigateToWeb(self.facebook_url)
            else:
                AbstractPage.logoutFacebook()
                
            # Login        
            self.homePageFacebook = self.loginPageFacebook.login(username, password)
            
            return self.homePageFacebook
        except Exception, e:
            Log.logError(str(e))
    
    # Login Twitter
    def loginTwitter(self, username, password, alreadyExistedAccount=False):
        try:
            self.loginPageTwitter = PageFactory.getTwitterLoginPage()
            
            if alreadyExistedAccount == False:
                AbstractPage.navigateToWeb(self.twitter_url)
            else:
                AbstractPage.logoutKlout()
            # Login
            self.homePageTwitter = self.loginPageTwitter.login(username, password)
    
            return self.homePageTwitter
        except Exception, e:
            Log.logError(str(e))
        
    # Logout Klout
    def logout(self, closeBrowser=True):
        try:
            if self.homePage == None:
                self.homePage = PageFactory.getHomePage()
                
            self.homePage.logoutKlout()
            
            if closeBrowser == True:
                AbstractPage.closeBrowser()
            else:
                self.loginPage = PageFactory.getLoginPage()
                return self.loginPage
        except Exception, e:
            Log.logError(str(e))
            
    # Logout Facebook
    def logoutFacebook(self, closeBrowser=True):
        try:
            if self.homePageFacebook == None:
                self.homePageFacebook = PageFactory.getFacebookHomePage() 
                
            self.homePageFacebook.logoutFacebook()
            
            if closeBrowser == True:
                AbstractPage.closeBrowser()
        except Exception, e:
            Log.logError(str(e))
            
    def logoutTwitter(self, closeBrowser=True):
        try:
            if self.homePageTwitter == None:
                self.homePageTwitter = PageFactory.getTwitterHomePage()
    
            self.homePageTwitter.logoutTwitter()
            
            if closeBrowser == True:
                AbstractPage.closeBrowser()
        except Exception, e:
            Log.logError(str(e))

    # Log in klout Tw/Fb without sign in
    def loginKloutWithoutAuthorize(self, connectType):
        try:
            self.loginPage = PageFactory.getLoginPage()
    
            AbstractPage.navigateToWeb(self.home_url)
            if (connectType == "twitter"):
                AbstractPage().clickElementByXPath(self.link_signintw_xpath)
            elif (connectType == "facebook"):
                AbstractPage().clickElementByXPath(self.link_signinfb_xpath)
            
            self.homePage = HomePageKlout()        
            return self.homePage
        except Exception, e:
            Log.logError(str(e))
    
    
    # Navigate to Twitter page and log out Twitter when Twitter 
    # account is already logged in 
    def logoutTwitterWithoutLogin(self):  
        # re-navigate to twitter site to logout for resolving "permission Denied" error           
        AbstractPage.navigateToWeb(self.twitter_url)
        self.homePageTwitter = PageFactory.getTwitterHomePage()           
        self.homePageTwitter.logoutTwitterWhenLoggedIn()
        Log.logInfo("Log out successfully")        

    # Run test suite by lib HTMLTestRunner
    @staticmethod
    def executeTestSuite_HTML(testSuite):
        testSuite = unittest.TestSuite()
        suite = unittest.TestLoader().loadTestsFromTestCase(testSuite)
        dateTime = time.strftime('%Y%m%d_%H_%M_%S')
        buf = file("test-reports/TestResults" + "_" + dateTime + ".html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
                        stream=buf,
                        title='Test Results',
                        description='Update_User_Settings'
                        )
        runner.run(suite)
        
    def closeBrowser(self):
        try:
            AbstractPage.closeBrowser()
        except Exception, e:
            Log.logError(str(e))
            
    def randomString(self, nStringLength):
        if AbstractPage.flag:
            try:
                return AbstractPage().getRandomString(nStringLength)
            except Exception, e:
                Log.logError(str(e))
#                
    @staticmethod         
    def writeTestReport(testModule):
        testmoduleName = str(testModule.__name__)
        testcases = XMLToExcelReport().getTestCases(testmoduleName)
        print testmoduleName

        
        suite = unittest.TestSuite()
        
        for testcase in testcases:
            suite.addTest(testModule(testcase))
            
#        dateTime = time.strftime('%Y%m%d_%H_%M_%S')
        dateTime = time.strftime('%m-%d-%Y')
        # verify test result folder is existed
        resultPath = DataConfig.getDataNode("report_path")
        
        if HubNode().use_grid == "No":
            browser = BrowserNoneGrid.browser
            version = BrowserNoneGrid.version
            if os.path.isdir(resultPath + "/" + "reports-" + browser + "-" + version):
                print "existed"
            else:
                print "make"
                os.mkdir(resultPath + "/" + "reports-" + browser + "-" + version)
    
            if os.path.isdir(resultPath + "/" + "reports-" + browser + "-" + version + "/" + dateTime):
                print "existed"
            else:
                print "make"
                
                os.mkdir(resultPath + "/" + "reports-" + browser + "-" + version + "/" +dateTime)
                
            runner = XMLTestRunner(file(resultPath+'/reports-%s-%s/%s/%s-%s.xml' % (browser,version,dateTime,testmoduleName,browser), "w"))
        else:
            args = sys.argv
            browser = args[2]
            port = args[1]
        
            if os.path.isdir(resultPath + "/" + "reports-" + browser + "-" + port):
                print "existed"
            else:
                print "make"
                os.mkdir(resultPath + "/" + "reports-" + browser + "-" + port)
    
            if os.path.isdir(resultPath + "/" + "reports-" + browser + "-" + port + "/" + dateTime):
                print "existed"
            else:
                print "make"
                
                os.mkdir(resultPath + "/" + "reports-" + browser + "-" + port + "/" +dateTime)
                
            runner = XMLTestRunner(file(resultPath+'/reports-%s-%s/%s/%s-%s.xml' % (browser,port,dateTime,testmoduleName,browser), "w"))
        
        runner.run(suite)