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
        sleep(3)

    def buyYoubei(self):
        driver=self.driver
        driver.touch('drag',{'fromX':325,'fromY':500,'toX':55,'toY':500})
        sleep(3)
        driver.touch('drag',{'fromX':325,'fromY':500,'toX':55,'toY':500})
        sleep(3)
        driver.touch('drag',{'fromX':325,'fromY':500,'toX':55,'toY':500})
        sleep(4)
        driver.element_by_class_name('XCUIElementTypeButton').click()
        sleep(3)
        #登录
        driver.element_by_xpath('//XCUIElementTypeButton[@name="登录"]').click()
        sleep(2)
        mo=driver.element_by_class_name('XCUIElementTypeTextField')
        mo.click()
        mo.send_keys('13711579877')
        driver.element_by_name('Done').click()
        sleep(1)
        pwd=driver.element_by_class_name('XCUIElementTypeSecureTextField')
        pwd.click()
        pwd.send_keys('0422wxl')
        driver.element_by_name('Done').click()
        #name=登录
        driver.element_by_xpath('//XCUIElementTypeButton[@name="登录"]').click()
        sleep(3)
        #driver.element_by_name('取消').click()
        #xpath name=null
        cancel=driver.element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]\
            /XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]')
        cancel.click()
        sleep(3)
        driver.element_by_name('投资').click()
        sleep(3)
        driver.element_by_name('优贝').click()
        sleep(3)
        driver.element_by_name('测试返现：现金').click()
        sleep(3)
        driver.element_by_name('立即投资').click()
        sleep(3)
        amount=driver.element_by_class_name('XCUIElementTypeTextField')
        amount.click()
        amount.send_keys('2000')
        driver.element_by_name('Done').click()
        sleep(2)
        #without eBei
        driver.element_by_name('Button').click()
        sleep(2)
        #coupon
        #driver.element_by_name('请选择投资券').click()
        #sleep(2)
        #100Yuan coupon
        #driver.element_by_name('50元投资券').click()
        #sleep(1)
        #payment method
        driver.element_by_name('选择支付方式').click()
        sleep(2)
        #balance
        driver.element_by_name('本金账户（元）').click()
        sleep(1)
        #xinzhibao
        #driver.element_by_name('薪智宝（元）').click
        #sleep(1)
        #bankcard
        #driver.element_by_name('工商银行 (尾号3443)').click()
        #sleep(1)
        #I agree
        driver.element_by_name('d9').click()
        driver.element_by_name('立即支付').click()
        sleep(3)
        driver.element_by_name('知道了').click()
        sleep(3)
        driver.element_by_name('我的').click()
        sleep(3)
        #scroll here
        driver.touch('drag',{'fromX':160,'fromY':600,'toX':160,'toY':400})
        sleep(2)
        driver.element_by_name('优贝赚呗投资记录').click()
        sleep(3)       
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_037_inv_records_macaca.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.element_by_name('投资测试返现：现金').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_037_invest_detail_macaca.png'
        driver.save_screenshot(sf3)
        sleep(2)
        driver.element_by_name('leftback').click()
        sleep(2)
        driver.element_by_name('leftback white').click()
        sleep(2)
        #balance
        driver.element_by_name('账户余额').click()
        sleep(2)
        driver.element_by_name('查看余额明细').click()
        sleep(2)
        driver.element_by_name('收益').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_037_income_records_macaca.png'
        driver.save_screenshot(sf1)
        sleep(2)
        driver.element_by_class_name('XCUIElementTypeCell').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_037_income_detail_macaca.png'
        driver.save_screenshot(sf0)
        sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(AppP2b('buyYoubei'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_037_macaca_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='51p2b of App environment iOS10.3(投资返现现金优贝产品(用账户余额支付)) test case report by Macaca',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
