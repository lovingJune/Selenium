'''
Created on Aug 28, 2012

@author: vu.dao
'''
from page.AbstractPage import AbstractPage
from page.facebook.AccountSettingPageFB import AccountSettingPageFB
from reportlog.Log import Log


class HomePageFB(AbstractPage):

    def __init__(self):
        '''
        Constructor
        '''
        self.btn_home_id = "navHome"
        self.btn_dropMenu_id = "userNavigationLabel"
        self.link_accountSetting_xpath = ".//*[@id='userNavigation']/li/a[text()='Account Settings']"
        self.link_logout_xpath = "//input[@value='Log Out']"
        self.txt_user = "email"
        
    def openAccountSettingPage(self):
        if AbstractPage.flag:
          
            # click dropdown menu
            self.clickElementById(self.btn_dropMenu_id)
            
            # Open Account Setting page
            self.clickElementByXPath(self.link_accountSetting_xpath)
                        
            Log.logError("Open account setting successfully")                      
            return AccountSettingPageFB()
            
            
    def getUserProfile(self):
        if AbstractPage.flag:
        
            # click dropdown menu
            self.clickElementById(self.btn_dropMenu_id)

            # Open Account Setting page
            self.clickElementByXPath(self.link_accountSetting_xpath)
            
            self.UserProfile = AccountSettingPageFB()
            
            return self.UserProfile.getUserSetting()