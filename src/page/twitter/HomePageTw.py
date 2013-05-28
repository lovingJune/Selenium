'''
Created on Sep 12, 2012

@author: tan.thanh.vo
'''
from page.AbstractPage import AbstractPage
from selenium.webdriver.common.action_chains import ActionChains
from reportlog.Log import Log

class HomePageTw(AbstractPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.btn_home_xpath = "//a[@data-nav='home']"
        self.btn_dropMenu_xpath = "//i[@class='nav-me']"
        self.link_accountSetting_xpath = "//ul[@class='dropdown-menu']/li/a[@data-nav='settings']"
        self.link_logout_xpath = "//ul[@class='dropdown-menu']/li/a[@data-nav='logout']"
        self.txt_user = "email"
        self.btn_dropMenuTW_xpath = "//*[@id='user-dropdown-toggle']/span[2]"
        self.btn_logoutTW_xpath = "//*[@id='signout-button']"
        self.btn_loginTW_xpath = "//*[@id='signin-link']/span"
                
    # log out Twitter without Login
    def logoutTwitterWhenLoggedIn(self):        
        if AbstractPage.flag:
            try:
                element01 = self.getElementByXPath(self.btn_dropMenuTW_xpath)
                element02 = self.getElementByXPath(self.btn_logoutTW_xpath)
                
                # Use ActionChains class to set click action for elements
                builder = ActionChains(AbstractPage.browser); 
                builder.click(element01);
                builder.click(element02);  
                
                # Execute javascript to click on element on Twitter Home page
                # Parameters:
                # first argument - The JavaScript to execute
                # second argument - The arguments to the script. May be empty
                AbstractPage().browser.execute_script("arguments[0].click();", element01)
                AbstractPage().browser.execute_script("arguments[0].click();", element02)                               
                
            except Exception, e:
                    Log.logError(str(e))
                    Log.logError("Log out unsuccessfully")                    
                    AbstractPage.flag = False
