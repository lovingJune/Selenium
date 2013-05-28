'''
Created on Aug 28, 2012

@author: vu.dao
'''
from page.AbstractPage import AbstractPage 
from page.facebook.HomePageFB import HomePageFB

class LoginPageFB(AbstractPage):

    def __init__(self):
        '''
        Constructor
        
        '''        
        self.txt_user_id = "email"
        self.txt_password_id = "pass"
        self.btn_login_id = "loginbutton"
        self.btn_allow_xpath = "//input[@value='Allow' and @type='submit']"
            
    def login(self, username, password):
        if AbstractPage.flag:
       
            # Input username
            self.sendKeyById(self.txt_user_id, username)
               
            # Input password         
            self.sendKeyById(self.txt_password_id, password)
               
            # Click on login button         
            self.clickElementById(self.btn_login_id)           
            
        return HomePageFB()        