'''
Created on Sep 12, 2012

@author: tan.thanh.vo
'''
from page.AbstractPage import AbstractPage 
from page.twitter.HomePageTw import HomePageTw

class LoginPageTw(AbstractPage):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''        
        self.txt_user_xpath = "//div[@class='placeholding-input username']//input[@class='text-input email-input']"
        self.txt_password_xpath = "//div[@class='placeholding-input password flex-table-form']/input[@class='text-input flex-table-input']"
        self.btn_login_xpath = "//button[@class='submit btn primary-btn flex-table-btn js-submit']"
            
    def login(self, username, password):
        if AbstractPage.flag:
           
            # Input username
            self.sendKeyByxPath(self.txt_user_xpath, username)
               
            # Input password         
            self.sendKeyByxPath(self.txt_password_xpath, password)
               
            # Click on login button         
            self.clickElementByXPath(self.btn_login_xpath)
                
        return HomePageTw()
