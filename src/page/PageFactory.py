'''
Created on Dec 13, 2012

@author: tinh.do
'''
from page.facebook.HomePageFB import HomePageFB
from page.facebook.LoginPageFB import LoginPageFB
from page.klout.LoginPageKlout import LoginPageKlout
from page.klout.HomePageKlout import HomePageKlout
from page.twitter.HomePageTw import HomePageTw
from page.twitter.LoginPageTw import LoginPageTw
from page.AbstractPage import AbstractPage
from page.twitter.LoginPageTw import LoginPageTw
from page.klout.SettingPageKlout import SettingPageKlout
from page.klout.FriendsPageKlout import FriendsPageKlout
from page.klout.DashboardPageKlout import DashboardPageKlout

class PageFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    ''' Factory methods to create page objects
    '''
    @staticmethod
    def getFacebookLoginPage():
        return LoginPageFB()
    
    @staticmethod
    def getFacebookHomePage():
        return HomePageFB()
    
    @staticmethod
    def getLoginPage():
        return LoginPageKlout()
    
    @staticmethod
    def getHomePage():
        return HomePageKlout()
    
    @staticmethod
    def getTwitterLoginPage():
        return LoginPageTw()
    
    @staticmethod
    def getTwitterHomePage():
        return HomePageTw()
    
    @staticmethod
    def getSettingPage():
        return SettingPageKlout()
    
    @staticmethod
    def getDashboardPage():
        return DashboardPageKlout()
    
    @staticmethod
    def getFriendPage():
        return FriendsPageKlout()