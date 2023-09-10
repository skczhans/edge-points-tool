import json
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

import time

def OpenUrl(url):
    # ������ַ
    driver.get(url)
    with open('cookies.txt', 'r') as f:  # ����webdriver����ʱ�����޺�ģʽ��ʹ�ô�cookie�ķ�ʽ��¼΢���˺�
        cookies_list = json.load(f)
        for cookie in cookies_list:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
            
def run_pc(random_number):
    #��������
    OpenUrl('https://cn.bing.com/search?q=' + str(random_number))
    
def getScore(str, l):
    times = 0
    for i in l:
        times += 1
        run_pc(i)
        print(str + "��" , times, ' done')
        time.sleep(2)
    driver.quit()
    
if __name__ == "__main__" :
    timeMobile = 30 #������������
    List = random.sample(range(1,10000),timeMobile) #�����������
    driverPath = './msedgedriver' #��������·��
    service = Service(driverPath = driverPath) #��������
    options = Options() #������ʼ��
    mobile_emulation = {"deviceName": "Galaxy Fold"}  # ����ƶ��豸��������
    options.add_experimental_option("mobileEmulation",mobile_emulation)  # ʹ���ƶ��豸����ģ������  
    driver = webdriver.Edge(service=service, options=options)
    getScore('Modile', List[:timeMobile])
    print('Modile done')
    
