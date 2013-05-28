'''
Created on Aug 28, 2012

@author: Vu Dao
'''
from page.AbstractPage import AbstractPage
from page.klout.HomePageKlout import HomePageKlout
import time
from reportlog.Log import Log

class LoginPageKlout(AbstractPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)

        self.btn_facebook_xpath = "//a[@class='fb-connect']"
        self.btn_twitter_xpath = "//a[@class='tw-connect']"
        self.btn_dropFacebook_xpath = "//a[@class='fb-sign-in-button']"
        self.btn_dropTwitter_xpath = "//a[@class='tw-sign-in-button']"
        self.link_signInHeader_xpath = "//span[text()='Sign In']"
        self.txt_username_id = "email"
        self.txt_password_id = "pass"
        self.txt_usernameTW_id = "username_or_email"
        self.txt_passwordTW_id = "password"
        self.txt_usernameFB_id = "email"
        self.txt_passwordFB_id = "pass"
        self.btn_login_id = "loginbutton"
        self.btn_loginTW_id = "allow"
        self.btn_loginFB_id = "loginbutton"       
        self.btn_home_id = "dashboard-menu-item"
        
    def loginKlout(self, username, password, connectType="facebook"):
        if AbstractPage.flag:    
            if connectType == "facebook":
                # Click on Facebook button
                self.clickElementByXPath(self.btn_facebook_xpath)
                
                # Input username
                self.sendKeyById(self.txt_username_id, username)
                
                # Input password
                self.sendKeyById(self.txt_password_id, password)
                
                # Click on Login button
                self.clickElementById(self.btn_login_id)
                
            if connectType == "twitter":
                # Click on Twitter button
                self.clickElementByXPath(self.btn_twitter_xpath)
                
                # Input user name
                self.sendKeyById(self.txt_usernameTW_id, username)
                
                # Input password
                self.sendKeyById(self.txt_passwordTW_id, password)
                
                # Click on Login button
                self.clickElementById(self.btn_loginTW_id)
                 
            return HomePageKlout()
    
    # Login with facebook and twitter button at drop menu
    def loginKlout_dropmenu(self, username, password, connectType="facebook"):
        if AbstractPage.flag:
            if connectType == "facebook":
                
                # Move mouse to Sign In link on header
                self.mouseMoveToElementByXpath(self.link_signInHeader_xpath)
                                    
                # Click on Facebook button
                self.clickElementByXPath(self.btn_dropFacebook_xpath)
                
                # Input username
                self.sendKeyById(self.txt_username_id, username)
                
                # Input password
                self.sendKeyById(self.txt_password_id, password)
                
                # Click on Login button
                self.clickElementById(self.btn_login_id)
                
            if connectType == "twitter":
                # Move mouse to Sign In link on header
                self.mouseMoveToElementByXpath(self.link_signInHeader_xpath)
                                    
                # Click on Twitter button
                self.clickElementByXPath(self.btn_dropTwitter_xpath)

                # Input user name
                self.sendKeyById(self.txt_usernameTW_id, username)
                
                # Input password
                self.sendKeyById(self.txt_passwordTW_id, password)
                
                # Click on Login button
                self.clickElementById(self.btn_loginTW_id)
                
            return HomePageKlout()
        
    # Open Authorize Klout Page For Facebook/Twitter
    def openAuthorizeKlout(self, connectType="facebook"): 
        if AbstractPage.flag:
            if connectType == "facebook":
                # click on facebook button
                self.clickElementByXPath(self.btn_facebook_xpath)
            else:
                # click on Twitter button
                self.clickElementByXPath(self.btn_twitter_xpath)
    
    # check window Authorize Klout For Facebook/Twitter Exist after click Facebook/Twitter button
    def isAuthorizeKloutExist(self, typeConnect="facebook"):      
        if AbstractPage.flag:
            result = False  
            if (typeConnect == "facebook"):                     
                result = (self.checkControlExistedById(self.btn_loginFB_id) and self.checkControlExistedById(self.txt_usernameFB_id) and self.checkControlExistedById(self.txt_passwordFB_id))                    
            elif (typeConnect == "twitter"):
                result = self.checkControlExistedById(self.btn_loginTW_id) and self.checkControlExistedById(self.txt_usernameTW_id) and self.checkControlExistedById(self.txt_passwordTW_id)
            
            if result:
                Log.logInfo("Authorize Page is existed!")
            else:
                Log.logInfo("Authorize Page is not existed!")
                
            return result                
    
    #User is logged out completely.The FB Authorize page is returned to enter email and password
    def checkLogoutFacebookCompletly(self):
        if AbstractPage.flag:
            self.checkControlExistedById(self.txt_username_id)
            self.checkControlExistedById(self.txt_password_id)
            if self.checkControlStatus(self.txt_username_id, "enabled"):
                Log.logInfo("Logout facebook completely")
                return True
            else:
                Log.logInfo("Logout facebook imcompletely")
                return False                   
            
    def isLoginPageKloutExist(self):   
        if AbstractPage.flag:                                                                               
            if self.checkControlExistedByXpath(self.btn_facebook_xpath):
                Log.logInfo("Login Page Klout Existed")
                return True
            else:
                Log.logInfo("Login Page Klout is not existed")
                return False

    def isLogoutPageSuccessfully(self):
        if AbstractPage.flag:
            if self.checkControlExistedByXpath(self.btn_twitter_xpath):
                Log.logInfo("Logout facebook completely")
                return True
            else:
                Log.logInfo("Logout facebook imcompletely")
                return False