import json
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

import time

def OpenUrl(url):
    # 访问网址
    driver.get(url)
    with open('cookies.txt', 'r') as f:  # 由于webdriver启动时类似无痕模式，使用带cookie的方式登录微软账号
        cookies_list = json.load(f)
        for cookie in cookies_list:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
            
def run_pc(random_number):
    #生成链接
    OpenUrl('https://cn.bing.com/search?q=' + str(random_number))
    
def getScore(str, l):
    times = 0
    for i in l:
        times += 1
        run_pc(i)
        print(str + 'the' , times, ' done') 
        time.sleep(2)
    driver.quit()
    
if __name__ == "__main__" :
    timeMobile = 30 #设置搜索次数
    List = random.sample(range(1,10000),timeMobile) #生成随机数列
    driverPath = './msedgedriver' #设置驱动路径
    service = Service(driverPath = driverPath) #导入驱动
    options = Options() #参数初始化
    mobile_emulation = {"deviceName": "Galaxy Fold"}  # 添加移动设备搜索参数
    options.add_experimental_option("mobileEmulation",mobile_emulation)  # 使用移动设备搜索模拟器打开  
    driver = webdriver.Edge(service=service, options=options)
    getScore('Modile', List[:timeMobile])
    print('Modile done')
    
