'''
Created on Sep 14, 2012

@author: thuy.cao
'''

from page.AbstractPage import AbstractPage

class FBAuthorizationPage(AbstractPage):

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        
        # Interface definition
        self.btn_login_xpath = "//input[@name='login']"
        self.txt_email_xpath = "//input[@name='email']"
        self.txt_password_xpath = "//input[@name='pass']"
        
    def login(self, email, password):
        if AbstractPage.flag:
            
            # Enter email
            self.sendKeyByxPath(self, self.txt_email_xpath)
            # Enter password
            self.sendKeyByxPath(self, self.txt_password_xpath)
            # Click Login button
            self.clickElementByXPath(self, self.btn_login_xpath)    
            
