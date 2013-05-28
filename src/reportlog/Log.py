'''
Created on Dec 13, 2012

@author: tinh.do
'''
class Log():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    @staticmethod
    def logInfo(message):
        print "Info: %s" % message
    
    @staticmethod
    def logError(message):
        print "Error: %s" % message
        
    @staticmethod
    def logFail(message):
        print "Fail: %s" % message
        
    @staticmethod
    def logPass(message):
        print "Pass: %s" % message