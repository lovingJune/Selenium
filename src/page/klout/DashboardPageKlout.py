'''
Created on Sep 17, 2012

@author: vuong.van
'''
from page.AbstractPage import AbstractPage
from reportlog.Log import Log


class DashboardPageKlout(AbstractPage):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.btn_showMyScoreSummary_xpath = "//span[text()='Show My Score Summary']"
        self.chart_90DayScoreHistory_ID = "highcharts-0"
        self.lb_deltaDayValue_xpath = "//li[@class='delta day increase']/span[@class='delta-value']"
        self.lb_deltaDayTitle_xpath = "//li[@class='delta day increase']/span[@class='delta-title']"
        self.lb_deltaWeekValue_xpath = "//li[@class='delta week increase']/span[@class='delta-value']"
        self.lb_deltaWeekTitle_xpath = "//li[@class='delta week increase']/span[@class='delta-title']"
        
        self.lb_deltaMonthValue_xpath = "//li[@class='delta month increase']/span[@class='delta-value']"
        self.lb_deltaMonthTitle_xpath = "//li[@class='delta month increase']/span[@class='delta-title']"
        
        self.lb_deltaQuarterValue_xpath = "//li[@class='delta quarter increase']/span[@class='delta-value']"
        self.lb_deltaQuarterTitle_xpath = "//li[@class='delta quarter increase']/span[@class='delta-title']"
        
        self.graph_networksUsed_ID = "networks-used-graph"
        self.lbl_networkStatsTwitter_xpath = "//div[contains(@class,'network-stats twitter')]"
        self.lbl_networkStatsFacebook_xpath = "//div[contains(@class,'network-stats facebook')]"
        self.lbl_networkStatsGoogleplus_xpath = "//div[contains(@class,'network-stats gplus')]"
        self.lbl_networkStatsLinkedin_xpath = "//div[contains(@class,'network-stats linkedin')]"
        self.lbl_networkStatsFoursquare_xpath = "//div[contains(@class,'network-stats foursquare')]"
        self.lbl_networkStatsKlout_xpath = "//div[contains(@class,'network-stats klout')]"
        
    def is90DayScoreHistoryExist(self):   
        if AbstractPage.flag:                                                                                            
            if self.checkControlExistedById(self.chart_90DayScoreHistory_ID):
                Log.logInfo("90 day score history is existed!")
                return True
            else:
                Log.logInfo("90 day score history is not existed!")
                return False
                
    def isDeltaDayExist(self):   
        if AbstractPage.flag:                                                                           
            if self.checkControlExistedByXpath(self.lb_deltaDayValue_xpath) and self.checkControlExistedByXpath(self.lb_deltaDayValue_xpath):
                Log.logInfo("Delta day is existed!")
                return True
            else:
                Log.logInfo("Delta day is not existed!")
                return False             
            
    def isDeltaWeekExist(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedByXpath(self.lb_deltaWeekValue_xpath) and self.checkControlExistedByXpath(self.lb_deltaWeekTitle_xpath):
                Log.logInfo("Delta Week is existed!")
                return True
            else:
                Log.logInfo("Delta Week is not existed!")
                return False
    
    def isDeltaMonthExist(self):   
        if AbstractPage.flag:                                                                               
            if self.checkControlExistedByXpath(self.lb_deltaMonthValue_xpath) and self.checkControlExistedByXpath(self.lb_deltaMonthTitle_xpath):
                Log.logInfo("Delta Month is existed!")
                return True
            else:
                Log.logInfo("Delta Month is not existed!")
                return False
            
    def isDeltaQuarterExist(self):   
        if AbstractPage.flag:                                                                               
            if self.checkControlExistedByXpath(self.lb_deltaQuarterValue_xpath) and self.checkControlExistedByXpath(self.lb_deltaQuarterTitle_xpath):
                Log.logInfo("Delta Quarter is existed!")
                return True
            else:
                Log.logInfo("Delta Quarter is not existed!")
                return False
    
    def isNetworkUsedExist(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedById(self.graph_networksUsed_ID):
                Log.logInfo("Network used graph is existed!")
                return True
            else:
                Log.logInfo("Network used graph is not existed!")
                return False
            
    def isNetworkStatsTwitterExist(self):   
        if AbstractPage.flag:                                                                             
            if self.checkControlExistedByXpath(self.lbl_networkStatsTwitter_xpath):
                Log.logInfo("Network stats Twitter is existed!")
                return True
            else:
                Log.logInfo("Network stats Twitter is not existed!")
                return False
            
    def isNetworkStatsFacebookExist(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedByXpath(self.lbl_networkStatsFacebook_xpath):
                Log.logInfo("Network stats Facebook is existed!")
                return True
            else:
                Log.logInfo("Network stats Facebook is not existed!")
                return False
    
    def isNetworkStatsGooglePlusExist(self):   
        if AbstractPage.flag:                                                                           
            if self.checkControlExistedByXpath(self.lbl_networkStatsGoogleplus_xpath):
                Log.logInfo("Network stats google plus is existed!")
                return True
            else:
                Log.logInfo("Network stats google plus is not existed!")
                return False       
    
    def isNetworkStatsLinkedinExist(self):   
        if AbstractPage.flag:                                                                               
            if self.checkControlExistedByXpath(self.lbl_networkStatsLinkedin_xpath):
                Log.logInfo("Network stats linkedin is existed!")
                return True
            else:
                Log.logInfo("Network stats linkedin is not existed!")
                return False
            
    def isNetworkStatsFoursquareExist(self):   
        if AbstractPage.flag:                                                                             
            if self.checkControlExistedByXpath(self.lbl_networkStatsFoursquare_xpath):
                Log.logInfo("Network stats foursquare is existed!")
                return True
            else:
                Log.logInfo("Network stats foursquare is not existed!")
                return False
            
    def isNetworkStatsKloutExist(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedByXpath(self.lbl_networkStatsKlout_xpath):
                Log.logInfo("Network stats klout is existed!")
                return True
            else:
                Log.logInfo("Network stats klout is not existed!")
                return False                       
    
    def openShowMyScoreSummary(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_showMyScoreSummary_xpath)
                    