#coding=UTF-8
from macaca import WebDriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common.action_chains import ActionChains

desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '10.3',
        'deviceName': 'iPhone 6',
        'app': os.path.abspath('/Users/samwang/Desktop/macaca_ios/PJS.app'),
        #'autoAcceptAlerts': 'true',
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class AppP2b(unittest.TestCase):

    def setUp(self):
        # set up macaca
        self.driver = WebDriver(desired_caps, server_url)
        self.driver.init()
        sleep(5)

    def login(self):
        driver=self.driver
        
        driver.swipe(325,500,55,500,1000)
        sleep(3)
        driver.swipe(325,500,55,500,1000)
        sleep(3)
        driver.swipe(325,500,55,500,1000)
        sleep(3)
        driver.element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]\
        /XCUIElementTypeScrollView[1]/XCUIElementTypeImage[1]/XCUIElementTypeButton[1]").click()
        sleep(5)
        #登录
        driver.element_by_name("登录").click()
        sleep(3)
        mo=driver.element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]\
        /XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]")
        mo.click()
        mo.send_keys("13816032863")
        driver.element_by_name("Done").click()
        sleep(1)
        pwd=driver.element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]\
        /XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField[1]")
        pwd.click()
        pwd.send_keys("0422wxl")
        driver.element_by_name("Done").click()
        #name=登录
        driver.element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]\
        /XCUIElementTypeScrollView[1]/XCUIElementTypeButton[2]").click() 
        sleep(2)
        #driver.element_by_name("取消").click()
        #xpath name=null
        cancel=driver.element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]\
        /XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]")
        cancel.click()
        sleep(3)     
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf2="./"+now+"_test_macaca.png"
        driver.save_screenshot(sf2)
        sleep(2)

        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(AppP2b("login"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename="./"+now+"_test_macaca_result.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title='51p2b of App environment iOS10.3(login)) test case report by Macaca',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
