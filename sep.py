from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By  # 导入By
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from parse import parse, is_login
import chat

class Sep:
    def __init__(self):
        # 创建EdgeOptions对象
        edge_options = webdriver.EdgeOptions()

        # 添加选项以隐藏浏览器窗口
        edge_options.add_argument('--headless')
        edge_options.add_argument('--disable-gpu')  # 如果需要，可以添加此选项以禁用GPU加速
        # 创建Edge WebDriver并传入选项
        self.driver = webdriver.Edge(options=edge_options)
        self.url = 'https://sep.ucas.ac.cn/'
        # 添加Cookie
        self.driver.get(self.url)
    
    def login(self, sepuser, JSESSIONID):
        cookie = {
        'domain': '.ucas.ac.cn',
        'name': 'sepuser',
        'value': sepuser,
        'Path': '/',
        }
        self.driver.add_cookie(cookie)
        print(sepuser,JSESSIONID)
        cookie = {
            'domain': '.ucas.ac.cn',
            'name': 'JSESSIONID',
            'value': JSESSIONID,
            'Path': '/',
        }
        self.driver.add_cookie(cookie)
        self.driver.get(self.url + 'appStore')
        self.driver.get(self.url + '/portal/site/226/821')
        time.sleep(3) 
        
        html = self.driver.page_source
        # return True
        if is_login(html):
            self.driver.get('https://jwxkts2.ucas.ac.cn/courseManage/selectCourse')
            return True
        return False
    
    def listen(self):
        print('listen')
        while True:
            yield self.query(is_test=False)
            time.sleep(2)
    
    def query(self, is_test=True):
        courseCode_field = self.driver.find_element(By.NAME, 'courseCode')
        courseCode_field.clear()
        courseCode_field.send_keys(self.courseCode)
        
        courseName_field = self.driver.find_element(By.NAME, 'courseName')
        courseName_field.clear()
        courseName_field.send_keys(self.courseName)
        
        # time.sleep(1) 

        x = self.driver.find_element(By.ID, 'para_list_chosen')
        x.click()
        time.sleep(0.5)
        li_element = self.driver.find_element(By.XPATH, f'//li[text()="{self.courseSchool}"]')
        li_element.click()

        # time.sleep(1) 
    
        form = self.driver.find_element(By.NAME, 'regfrm2') 
        
        form.submit()
        time.sleep(1)
        # 获取JavaScript执行后的HTML
        html = self.driver.page_source
        return parse(html, is_test, self)
    
    def add_course(self, courseCode, courseSchool, courseName, interval, username, wechat_path):
        self.courseCode = courseCode
        self.courseSchool = courseSchool
        self.courseName = courseName
        self.interval = interval
        self.username = username
        self.wechat_path = wechat_path
        